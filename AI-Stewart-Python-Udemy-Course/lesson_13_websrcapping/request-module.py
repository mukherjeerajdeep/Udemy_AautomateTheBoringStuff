import requests

response = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(response.status_code)

print(response.text)