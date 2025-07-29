import requests
import csv
import pandas as pd
import json

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
                'movie_id': result['id'],
                'vote_count': result['vote_count'],
                'average_rating': result['vote_average']
            }
            completed_movies.append(movie_info)

        page += 1
    return completed_movies
            

def get_distribution(column):
    counts = column['rating'].value_counts().reindex(range(5, 11), fill_value=0)
    return counts.to_dict()


movies = get_movies_id(10)

df = pd.read_csv('movie_reviews.csv')

# rating 정제
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
df = df.dropna(subset=['rating'])
df['rating'] = df['rating'].astype(int)

rating_distribution = df.groupby('movie_id').apply(get_distribution).to_dict()

for movie in movies:
    movie_id = movie['movie_id']
    distribution = rating_distribution.get(movie_id, {str(i): 0 for i in range(5, 11)})

    movie['rating_distribution'] = json.dumps({
        str(k): v for k, v in distribution.items()
    }, ensure_ascii=False)


fields = ["movie_id", "average_rating", "vote_count", "rating_distribution"]



with open('movie_ratings.csv', 'w', newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(movies)
