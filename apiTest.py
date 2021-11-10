import requests

url = 'https://jsonplaceholder.typicode.com/posts'

res = requests.get(url)
# print(res.status_code)

datum = res.json()[0]
print(datum)
print(datum['id'])

url = 'https://jsonplaceholder.typicode.com/posts'
params = {
    "id": 3
}

res = requests.get(url, params)
print(res.status_code)
print(res.json())
