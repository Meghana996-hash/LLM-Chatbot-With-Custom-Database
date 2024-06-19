import chromadb as crdb
import json

with open("example.json",'r') as f:

    examples = json.load(f)

client = crdb.PersistentClient("examples")
try:
    collection = client.get_collection("sample_queries")
except:
    collection = client.create_collection("sample_queries")
    with open("example.json", "r") as f:
        data = json.load(f)

    for id,pair in enumerate(data['example_pairs']):
        collection.add(
            ids=str(id),
            documents=pair['nl_query']
        )

def query_from_vectordb(user_query):

    res = collection.query(query_texts=user_query, n_results=1)
    print(res)

    return res['documents'][0][0], examples['example_pairs'][int(res['ids'][0][0])]['sql_query']

def add_example_pairs(nl_query,sql_query):

    """Adding of natural language and corresponding SQL query in the vector database.
    
    Args:
        nl_query: natural language query
        sql_query: corresponding sql query
    
    Returns: None
    """
    new_example = {
        "nl_query": nl_query,
        "sql_query": sql_query
        }
    # Load the existing data from the JSON file
    with open("example.json", "r") as f:
        data = json.load(f)

    # Add the new example pair to the data
    data["example_pairs"].append(new_example)

    # Save the updated data back to the JSON file
    with open("example.json", "w") as f:
        json.dump(data, f, indent=4)

    id = int(collection.get()['ids'][-1])

    collection.add(
        ids=str(id+1),
        documents=nl_query
    )
    

# nl_query,sql_query = query_from_vectordb(input("Ask your query:\n"))
# print(f'NL Query: {nl_query}\nSQL Query: {sql_query}')
# print(res['documents'][0][0])
# print(examples['example_pairs'][int(res['ids'][0][0])]['sql_query'])
