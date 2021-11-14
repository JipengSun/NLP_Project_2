from bs4 import BeautifulSoup
import requests
import classes

url = "https://www.allrecipes.com/recipe/230103/buttery-garlic-green-beans/"

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
ingredients_data = soup.find(class_='ingredients-section')
ingredients = []

ingredient_names = soup.find_all(class_ = 'ingredients-item')
# print(ingredient_names)
for i in ingredient_names:
    target = i.find(class_ = 'checkbox-list-input')
    x = classes.Ingredient(target.get('value'))
    x.set_quantity(target.get('data-init-quantity'))
    x.set_unit(target.get('data-unit'))
    # print(i.get('data-ingredient'))
    ingredients.append(x)

print(ingredients)
    
