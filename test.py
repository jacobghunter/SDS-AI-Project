import requests

with open('test.html', 'r') as f:
    html = f.read()

# print(requests.get('http://localhost:5000/article'))
req = requests.get('http://167.99.111.147/article')
# req = requests.get('http://localhost:8000/article')
print(req.text)
# req = requests.post('http://localhost:5000/delete_article', json={"article": "Hello, World!"})

# print(req)