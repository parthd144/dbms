from collections import defaultdict

def mapper(person):
    profession = person['profession']
    name = person['name']
    yield profession, name

def reducer(profession, names):
    return (profession, list(names))

def map_reduce(people):
    intermediate = mapper(people)
    results = defaultdict(list)
    for profession, name in intermediate:
        results[profession].append(name)
    return [(profession, reducer(profession, names)) for profession, names in results.items()]

# Input Data
people = [
    {'person_id': 1, 'name': 'John', 'addr': 'USA', 'profession': 'Engineer'},
    {'person_id': 2, 'name': 'Alice', 'addr': 'UK', 'profession': 'Doctor'},
    {'person_id': 3, 'name': 'Bob', 'addr': 'USA', 'profession': 'Engineer'},
    {'person_id': 4, 'name': 'Chris', 'addr': 'Canada', 'profession': 'Doctor'},
]

# Perform MapReduce operation
results = map_reduce(people)

# Print Results
for result in results:
    print(f"Profession: {result[0]}, People: {result[1]}")