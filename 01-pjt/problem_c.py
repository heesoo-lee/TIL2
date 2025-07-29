import requests
import csv

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

# movie_id를 사용해 reivew 정보를 추출하는 함수
def get_reviews(movie_list):

    movie_reviews = []

    for movie in movie_list:
        movie_id = movie['id']
        title = movie['title']
        url = f'{BASE_URL}/movie/{movie_id}/reviews'
        params = {'api_key': API_KEY}
        
        response = requests.get(url, params=params)
        data = response.json()

        results = data.get('results', [])

        no_review = {
            'movie_id' : movie_id,
            'review_id': None,
            'author': None,
            'content': '내용 없음',
            'rating': None
        }

        if results:
            for result in results:
                review_info = {
                    'movie_id': movie_id,
                    'review_id': result.get('id'),
                    'author': result.get('author'),
                    'content': result.get('content', '').strip().replace('\n', ' '),
                    'rating': result.get('author_details', {}).get('rating')
                }
                movie_reviews.append(review_info)
        else:
            movie_reviews.append(no_review)
        
    return movie_reviews
            

movies = get_movies_id(10)

processed_movies = []
for movie in movies:

    result = {
        'id': movie['id'],
        'title': movie['title']
    }
    processed_movies.append(result)

fields = ["movie_id", "review_id", "author", "content", "rating"]

with open('movie_reviews.csv', 'w', newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(get_reviews(processed_movies))



# mid = 1124619
# print(get_movie_title(mid))