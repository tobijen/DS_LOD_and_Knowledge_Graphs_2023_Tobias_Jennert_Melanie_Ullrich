import pandas as pd
import numpy as np
import os
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pathlib import Path
import random


from helpers.df_helpers import documents2Dataframe
from helpers.df_helpers import df2Graph
from helpers.df_helpers import graph2Df

## Input data directory
data_dir = "abstract_input"
inputdirectory = Path(f"./data/{data_dir}")
## This is where the output csv files will be written
out_dir_raw = 'abstract_output'
outputdirectory = Path(f"./data/{out_dir_raw}")

out_dir_processed = 'abstract_output_processed'
outputdirectory_processed_graph_data = Path(f"./data/{out_dir_processed}")

## Load data
loader = DirectoryLoader(inputdirectory, show_progress=True)
documents = loader.load()


## Split input data into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500,
    chunk_overlap=150,
    length_function=len,
    is_separator_regex=False,
)

pages = splitter.split_documents(documents)
print("Number of chunks = ", len(pages))
print(pages[4].page_content)
print(pages[4].metadata)


# Create a dataframe of all the chunks
df = documents2Dataframe(pages)
print(df.shape)
print(df.head())

print("DF: ", df[:1])


## Extract concepts
## To regenerate the graph with LLM, set this to True
regenerate = False

if regenerate:
    concepts_list = df2Graph(df[:10], model='zephyr:latest')
    dfg1 = graph2Df(concepts_list)
    if not os.path.exists(outputdirectory):
        os.makedirs(outputdirectory)
    
    dfg1.to_csv(outputdirectory/"graph.csv", sep="|", index=False)
    df.to_csv(outputdirectory/"chunks.csv", sep="|", index=False)
else:
    dfg1 = pd.read_csv(outputdirectory/"graph.csv", sep="|")

dfg1.replace("", np.nan, inplace=True)
dfg1.dropna(subset=["node_1", "node_2", 'edge'], inplace=True)
dfg1['count'] = 4 
## Increasing the weight of the relation to 4. 
## We will assign the weight of 1 when later the contextual proximity will be calculated.  
print(dfg1.shape)
dfg1.head()

## Calculating contextual proximity
def contextual_proximity(df: pd.DataFrame) -> pd.DataFrame:
    ## Melt the dataframe into a list of nodes
    dfg_long = pd.melt(
        df, id_vars=["chunk_id"], value_vars=["node_1", "node_2"], value_name="node"
    )
    dfg_long.drop(columns=["variable"], inplace=True)
    # Self join with chunk id as the key will create a link between terms occuring in the same text chunk.
    dfg_wide = pd.merge(dfg_long, dfg_long, on="chunk_id", suffixes=("_1", "_2"))
    # drop self loops
    self_loops_drop = dfg_wide[dfg_wide["node_1"] == dfg_wide["node_2"]].index
    dfg2 = dfg_wide.drop(index=self_loops_drop).reset_index(drop=True)
    ## Group and count edges.
    dfg2 = (
        dfg2.groupby(["node_1", "node_2"])
        .agg({"chunk_id": [",".join, "count"]})
        .reset_index()
    )
    dfg2.columns = ["node_1", "node_2", "chunk_id", "count"]
    dfg2.replace("", np.nan, inplace=True)
    dfg2.dropna(subset=["node_1", "node_2"], inplace=True)
    # Drop edges with 1 count
    dfg2 = dfg2[dfg2["count"] != 1]
    dfg2["edge"] = "contextual proximity"
    return dfg2


dfg2 = contextual_proximity(dfg1)
dfg2.tail()

## Merge both the dataframes

dfg = pd.concat([dfg1, dfg2], axis=0)
dfg = (
    dfg.groupby(["node_1", "node_2"])
    .agg({"chunk_id": ",".join, "edge": ','.join, 'count': 'sum'})
    .reset_index()
)

print(dfg)

dfg.to_csv(outputdirectory/"graph_processed.csv", sep="|", index=False)
