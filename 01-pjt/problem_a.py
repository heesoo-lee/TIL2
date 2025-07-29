# TMDB API 키 설정
import requests
from pprint import pprint


API_KEY = '23d68619b52bd424d2567f2aa27f6cc2'
BASE_URL = 'https://api.themoviedb.org/3'

# API 호출 함수
def get_movie():
    total_data = []
    for page in range(1, 50) : 
        url = f'{BASE_URL}/movie/popular?page={page}'
        params = {
            'api_key': API_KEY,
            'language': 'ko-KR'  # 한글 결과 원할 경우
        }
        response = requests.get(url, params=params).json()
        total_data.append(response)
    return total_data
# 영화 데이터 처리 함수
datas = get_movie()
temp_item = {}
complete_data = []
fields = ['id', 'title', 'release_date', 'popularity']


for page in datas :
    for movies in page['results'] :
        movie_info = {
            'id': movies['id'],
            'title': movies['title'],
            'release_date': movies['release_date'],
            'popularity': movies['popularity']
        }
        complete_data.append(movie_info)

pprint(complete_data)

# 데이터 수집 및 CSV 파일로 저장

import csv

with open('movies.csv', 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(complete_data)
