import requests

movie_ids = [
    238,
    680,
    550,
    185,
    641,
    515042,
    152532,
    120467,
    872585,
    906126,
    840430
]


# response = requests.get(....)
# data = response.json()
# https://nomad-movies.nomadcoders.workers.dev/movies/XXXX

for movie_id in movie_ids:
    response = requests.get(
        f"https://nomad-movies.nomadcoders.workers.dev/movies/{movie_id}")
    data = response.json()
    print(data)


print("---------------------------------------------------------------------")

for movie_info in movie_ids:
    response = requests.get(
        f"https://nomad-movies.nomadcoders.workers.dev/movies/{movie_info}")
    data = response.json()
    print(f" Movie_id : {data['id']} \n Title : {data['title']} \n Overview: {
          data['overview']} \n  Vote_average: {data['vote_average']} \n")