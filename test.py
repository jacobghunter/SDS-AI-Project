import requests

with open('test.html', 'r') as f:
    html = f.read()

# print(requests.get('http://localhost:5000/article'))
print(requests.post('http://localhost:5000/upload_article/test', data=html))
# req = requests.post('http://localhost:5000/delete_article', json={"article": "Hello, World!"})

# print(req)