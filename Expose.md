# Visualize OpenAlex data with Apache AGE

## Motivation
OpenAlex is a free and open catalog of the world's scholarly research system. The OpenAlex dataset describes scholarly and how those entities are connected to each other. Types of entities include works, authors, institutions, concepts, publishers, sources, and funders. This data can be explored and filtered in the web ui of OpenAlex. But the data is only presented as a table in the web ui and can be accessed in JSON-format over the API. So there is no way to deeply explore the data by aggregating and visualizing it to get a deeper understanding of the connections presented in that data.

## Methology
To visualize the data of OpenAlex we plan to integrate the data into a relational postgres database wich is extended with the Apache Age tool. Apache AGE is a tool to explore and visualize graph data inside a relational postgresql data base.

## Goals
The goal of this project is to make the data of OpenAlex more exploreable and get a deeper understanding of the data by visualizing it.

- Specific exploration and visualization goal is missing ?!

## Time schedule (Hard to define, because there is no deadline)

- 1 Week: Implementation of the data into the postgres database
- 1 Week: Implementing the Apache AGE Tool into Postgres and setup Apache AGE Viewer
- 1 Week: Implementing the data into the Apache AGE tool