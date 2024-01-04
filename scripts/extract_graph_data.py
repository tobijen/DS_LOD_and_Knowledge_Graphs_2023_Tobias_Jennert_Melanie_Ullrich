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
out_dir = 'abstract_output'
outputdirectory = Path(f"./data/{out_dir}")

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


## Extract concepts
## To regenerate the graph with LLM, set this to True
regenerate = True

if regenerate:
    concepts_list = df2Graph(df, model='zephyr:latest')
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