from pymongo import MongoClient

# Create a MongoDB client
client = MongoClient("mongodb://localhost:27017/")

# Create/get a database
db = client['mydatabase']

# Create/get a collection
collection = db['mycollection']

print("Connected to MongoDB!")

# Insert document - one and many
document1 = {"name": "Flo", "age": 25, "city": "Brussels"}
collection.insert_one(document1)

documents = [
    {"name": "Anna", "age": 28, "city": "Berlin"},
    {"name": "Greg", "age": 32, "city": "Ghent"},
]
collection.insert_many(documents)

print("Documents inserted!")

#  Find document - one and many
result = collection.find_one({"name": "John"})
print("Found one:", result)

results = collection.find()
for document in results:
    print(document)

# Update document - one and many
collection.update_one({"name": "John"}, {"$set": {"age": 26}})
print("Document updated!")

collection.update_many({"city": "London"}, {"$set": {"city": "Manchester"}})
print("Documents updated!")

# Delete document - one and many
collection.delete_one({"name": "John"})
print("Document deleted!")

collection.delete_many({"city": "Manchester"})
print("Documents deleted!")
