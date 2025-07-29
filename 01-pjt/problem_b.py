# TMDB API 키 설정
import requests
from pprint import pprint
import csv


API_KEY = '23d68619b52bd424d2567f2aa27f6cc2'
BASE_URL = 'https://api.themoviedb.org/3'

def get_popular_movies():
    total_data = []
    for page in range(1,10) : 
        url = f'{BASE_URL}/movie/popular?page={page}'
        params = {
            'api_key': API_KEY 
        }
        response = requests.get(url, params=params).json()
        total_data.append(response)
    return total_data

datas1 = get_popular_movies()

movie_id = []
original_title = []
for page in datas1 :
    for movies in page['results'] :
            movie_id.append(movies['id'])
            original_title.append(movies['original_title'].replace(' ', '-').lower())

print(movie_id)
print(original_title)
        
# # API 호출 함수
def get_movie_details():
    total_data = []
    import time
    for i in range(len(movie_id)):
        url = f'{BASE_URL}/movie/{movie_id[i]}-{original_title[i]}'
        params = {
            'api_key': API_KEY,
            'language': 'ko-KR'
        }
    
        resp = requests.get(url, params=params)
        response = resp.json()
        total_data.append(response)
    return total_data

datas2 = get_movie_details()
pprint(datas2)
temp_item = {}

complete_data = []
for movie in datas2:
    genres = movie.get('genres', [])
    genre_names = [g['name'] for g in genres if 'name' in g]
    movie_info = {
        'movie_id': movie.get('id'),
        'budget': movie.get('budget'),
        'revenue': movie.get('revenue'),
        'genres': genre_names
    }
    complete_data.append(movie_info)

with open('movie_details.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['movie_id', 'budget', 'revenue', 'genres'])
    writer.writeheader()
    for item in complete_data:
        writer.writerow(item)