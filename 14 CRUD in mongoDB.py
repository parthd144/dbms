from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['test']

#create collection
db.create_collection('person')

#insert data
person = {'person_id': 1, 'name': 'John', 'addr': 'USA', 'profession': 'Engineer'}
result = db.person.insert_one(person)
print("Data inserted with person_id:", person['person_id'])

#read data
for x in db.person.find():
 print("Person_id:", x['person_id'], "Name:", x['name'], "Address:", x['addr'], "Profession:", x['profession'])

#update data
result = db.person.update_one({'person_id': 1}, {'$set': {'name': 'Johnny', 'profession': 'Senior Engineer'}})
print("Data updated with person_id:", person['person_id'])

#delete data
result = db.person.delete_one({'person_id': 1})
print("Data deleted with person_id:", person['person_id'])