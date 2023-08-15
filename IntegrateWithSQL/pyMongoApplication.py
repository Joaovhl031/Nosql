import pymongo as pyM
import datetime
import pprint

client = pyM.MongoClient("mongodb+srv://joaovhl031:Joaohenrique1.@cluster1.7dnwvmk.mongodb.net/?retryWrites=true&w=majority")

db = client.test

collection = db.test_collection
print(db.test_collection)


post = {
    "autor": "Joao",
    "text": "Integração com MongoDB",
    "tags": ["python", "DataBases", "MongoDB"],
    "date": datetime.datetime.utcnow()
}


posts=  db.posts
post_id= posts.insert_one(post).inserted_id
print(post_id)

print("PPRINT EXECUTE")

pprint.pprint(db.posts.find_one())


new_posts = [{
            "autor":"Pedro",
            "texto":"Iam study for Software Developer",
            "tags":["ti", "developer", "software"],
            "date":datetime.datetime.utcnow()},
            {
            "autor":"Victor",
            "texto":"ESSE ERA MEU NOME DE NERD",
            "tags":["Gordao do pc","new_album","mtg"],
            "date": datetime.datetime(2023, 7, 21, 10, 45)
            }]

result = posts.insert_many(new_posts)
print(result.inserted_ids)


print("\nRecuperação final")
pprint.pprint(db.posts.find_one({"autor":"Victor"}))


print('\nDocumentos em Posts')
for post in posts.find():
    pprint.pprint(post)