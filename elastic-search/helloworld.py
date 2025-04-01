from elasticsearch import Elasticsearch

# Connect to Elasticsearch
es = Elasticsearch("http://localhost:9200")

# Index a document
doc = {"message": "Hello, World!", "timestamp": "2025-04-01T12:00:00"}
es.index(index="hello_world", id=1, document=doc)

# Retrieve the document
res = es.get(index="hello_world", id=1)
print("Stored Document:", res["_source"])

# Search for "Hello"
query = {"query": {"match": {"message": "Hello"}}}
search_res = es.search(index="hello_world", body=query)
print("Search Results:", search_res["hits"]["hits"])
