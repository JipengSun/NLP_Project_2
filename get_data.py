from bs4 import BeautifulSoup
import requests

url = "https://www.allrecipes.com/recipe/230103/buttery-garlic-green-beans/"

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
ingredients_data = soup.find_all(class_='ingredients-section')
ingredients = []

print(ingredients_data)
