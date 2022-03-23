import requests
import bs4

result = requests.get("http://www.example.com/")
type(result)

soup = bs4.BeautifulSoup(result.text, "lxml")

# This will print the whole content but with
# print(result.text)
# print(soup)
print(result.raise_for_status())

