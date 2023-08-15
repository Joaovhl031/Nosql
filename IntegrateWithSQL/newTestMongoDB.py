import pymongo as pyM
import pprint, pymongo 


client = pyM.MongoClient("mongodb+srv://joaovhl031:Joaohenrique1.@cluster1.7dnwvmk.mongodb.net/?retryWrites=true&w=majority")
db = client.test
posts= db.posts

print('\nDocumentos em Posts')
for post in posts.find():
    pprint.pprint(post)

print(posts.count_documents({"autor": "Joao"}))
print(posts.count_documents({"tags": "insert"}))

pprint.pprint(posts.find_one({"tags": "insert"}))

print("\nRecuperando documentos com sort")
for post in posts.find({}).sort("date"):
    pprint.pprint(post)

result = db.profiles.create_index([('author', pymongo.ASCENDING)], unique=True)

print(sorted(list(db.profiles.index_information())))

user_profile = [
    {"user_id":210, "nome":"Juan"},
    {"user_id":211, "nome":"Catarina"}
]

result = db.profile_user.insert_many(user_profile)

print("======================")
collections = db.list_collection_names()
for collection in collections:
    print(collection)


print(posts.delete_one({"autor":"Pedro"}))


client.drop_database('test')

print(db.list_collection_names())