# DS_LOD_and_Knowledge_Graphs_2023_Tobias_Jennert_Melanie_Ullrich

# Use poetry

run in shell

export PATH="/Users/tobiasjennert/.local/bin:$PATH"


## Doc

Api-Endpoint = https://api.openalex.org/works?sample=20

Interesting field in the data: abstract_inverted_index


Source:
- https://towardsdatascience.com/how-to-convert-any-text-into-a-graph-of-concepts-110844f22a1a
- https://docs.openalex.org/api-entities/works



## Project Planing

- Get abstract data from the open alex api ✅
- Extract the text from the api response ✅
- Store the abstract text in a txt file ✅
- Insert filters in the open alex url to get works for a specific topic
- Get Ollama running via the api
- Query Ollama for testing
