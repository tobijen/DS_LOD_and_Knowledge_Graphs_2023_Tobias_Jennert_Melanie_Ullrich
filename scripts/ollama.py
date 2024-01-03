import requests

url = "http://localhost:11434/api/generate"
data = {
    "model": "zephyr",
    "prompt": "Say: Hello World!"
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.text)