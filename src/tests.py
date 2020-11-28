import requests

for i in range(1):
    r = requests.post(
            url='http://localhost:8000/add',
            json={'keyword': 'Муха', 'location': 'Москва'}
    )
    print(r.content)
