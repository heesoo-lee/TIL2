import csv
from pprint import pprint

with open('movie_details.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    data_list = [row for row in csv_reader]

with open('movies.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    data_list2 = [row for row in csv_reader]

results_info = []
for item in data_list:
    item['budget'] = int(item['budget'])
    item['revenue'] = int(item['revenue']) 
    result = (item['revenue'] / int(item['budget']) if int(item['budget']) > 0 else 0)
    result_info = {
            'id': item['movie_id'],
            'result': result
        }
    results_info.append(result_info)
    
max_result = max(results_info, key=lambda x: x['result'])

for item in data_list2:
    if item['id'] == max_result['id']:
        print(f"영화 제목: {item['title']}, 영화 ID: {item['id']}, 수익률: {max_result['result']:.2f}")
# pprint(max_result)