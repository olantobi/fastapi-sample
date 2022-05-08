import requests

res = requests.post("http://127.0.0.1:8000/path", json = {"msg": "sample lowercase string"})

print(res.status_code)
print(res.json())