import csv
from pprint import pprint

with open('movie_cast.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    # print(csv_reader.fieldnames)
    data_list = [row for row in csv_reader]

movies = set([row['movie_id'] for row in data_list])

actor_id = []
actor_name = []

for movie in movies :
    actor_id = []
    for data in data_list :
        if data['movie_id'] == movie and data['\ufeffcast_id'] not in actor_id:
            actor_id.append(data['\ufeffcast_id'])
            actor_name.append(data['name'])

busy_actors = []
for name in set(actor_name):
    if actor_name.count(name) > 1:
        busy_actors.append(name)
print(busy_actors)