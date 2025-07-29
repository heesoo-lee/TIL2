import requests
import csv
from pprint import pprint

API_KEY = '584b4090fc6fc32ec9b9e2d8e74a5166'
BASE_URL = 'https://api.themoviedb.org/3'


completed_movies = []

# response로 받는 값들의 field 조사
def print_keys(obj, prefix=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            print(f"{prefix}{k} -> {type(v).__name__}")
            print_keys(v, prefix + k + ".")
    elif isinstance(obj, list):
        if obj:
            print(f"{prefix}[list:{len(obj)}]")
            print_keys(obj[0], prefix + "[0].")

# movie_id로 movie title 조회
def get_movie_title(movie_id, language="ko-KR"):
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {
        "api_key": API_KEY,
        "language": language
    }
    r = requests.get(url, params=params, timeout=10)
    if r.status_code == 404:
        return None  # 없는 ID
    r.raise_for_status()
    return r.json().get("title")

# movie_id, title 저장 함수
def get_movies_id(max_pages):
    page = 1

    while page <= max_pages:

        params = {
            'api_key': API_KEY,
            'vote_average.gte': 5,
            'page': page
        }
        response = requests.get(f'{BASE_URL}/discover/movie', params=params).json()
        results = response.get('results', [])
        for result in results:
            movie_info = {
                'id': result['id'],
                'title': result['title']
            }
            completed_movies.append(movie_info)

        page += 1
    return completed_movies

# movie_id를 사용해 review 정보를 추출하는 함수
def get_actor(movie_list):

    movie_actors = []

    for movie in movie_list:
        movie_id = movie['id']
        url = f'{BASE_URL}/movie/{movie_id}/credits'
        params = {'api_key': API_KEY}

        response = requests.get(url, params=params)
        data = response.json()

        results = data.get('cast', [])

        for result in results:
            if int(result.get('order')) <= 10:
                cast_info = {
                    'cast_id': result.get('id'),
                    'movie_id': movie_id,
                    'name': result.get('name', '').replace('\n', ' ').replace('\r', ' ').strip(),
                    'character': result.get('character', '').replace('\n', ' ').replace('\r', ' ').strip(),
                    'order': result.get('order')
                }
                movie_actors.append(cast_info)
        
    return movie_actors

movies = get_movies_id(1)


fields = ["cast_id", "movie_id", "name", "character", "order"]

with open('movie_cast.csv', 'w', newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(get_actor(movies))



# mid = 1124619
# print(get_movie_title(mid))