#tranformations
import json
from nltk.probability import DictionaryConditionalProbDist
import get_recipe_json


def input_check(type, bound):
    #takes 'num' (for now, maybe add str later), and bound (the max size the number can be)
    invalid_message = "Invalid choice. Please try again."
    while True:
        x = input("> ")
        if type == "num":
            if x.isdigit():
                if int(x) > bound:
                    print(invalid_message) 
                else:
                    print("\n")
                    return x
            else: print(invalid_message)


def make_vegetarian(recipe_url):
    meats_dict = ['chicken', 'beef', 'pork', 'lamb', 'fish', 'salmon', 'Prosciutto']
    meat_alternatives = ['tofu', 'beans', 'lentils']
    #get type of alternative

    print("\nWhat kind of meat alternative would you like? (enter number)\n")
    for alt in range(len(meat_alternatives)):
        print(str(alt) + ": " + meat_alternatives[alt] + "\n")

    meat_alt = input_check('num', 2)
    meat_alt = meat_alternatives[int(meat_alt)]

    #get recipe
    recipe_data = get_recipe_json.get_recipe_json(recipe_url)
    



    #fix name
    recipe_name = recipe_data['name']
    removed_meats = []
    for meat in meats_dict:
        recipe_name = recipe_name.replace(meat, meat_alt)
        removed_meats.append(meat)
    recipe_data['name'] = recipe_name

    #fix ingredients
    for ingredient in recipe_data['ingredients']:
        for meat in removed_meats:
            if meat.lower() in ingredient['name'].lower():
                ingredient['name'] = meat_alt
                #what to do with units?
                ingredient['unit'] = ''
                ingredient['quantity'] = ''

    print(recipe_data)
    #fix steps
   

    
    #go through ingredients, replace meats with selected alternative [maybe]
    #go through steps, replace meats with selected alternatives
    #look at quantities and maybe change if it says "1 piece of chicken"

    #what if it says 'chicken breast'? use dependency parser? to replace both at the same time
    #print what the changes we made were - maybe call function to print out original recipe
    #print all transformed steps

    return 

def make_healthy(recipe_data):
    #replace unhealthy foods with healthy alternatives
    #replace frying with alternative method
    sugar = []
    unhealthy_oil = []
    trans_fat = ['vegetable oil','fried food','chips','creamer','margarine']
    saturated_fat = ['cheese','coconut oil','whole milk','red meat']
    salt = []

    unhealthy_ingredient_data = {
        "sugar":[],
        "fat":[],
        "red meat":[]
    }

    vegetables = []
    fruits = []
    grains = ['quinoa','corn','millet','brown rice']
    protein = ['lean meat','eggs','nuts','seeds','soy products']
    healthy_oil = ['olive','flaxseed','canola','aocado']

    healthy_ingredient_data = {
        "vegetables"
    }

    for step in recipe_data['steps']:
        print (step)
        


def make_indian(recipe):
    #remove all spices, replace with indian spices
    #[remove certain meats, replace with others?]

    #dictionary

    #no beef, use spices (red chile powder [paste], curry powder, masala)
    #mostly eat chicken

    return

def make_kosher(recipe):
    return

def make_gluten_free(recipe):
    return

def make_dairy_free(recipe):
    return


### optional
def scale_recipe(recipe, scale):
    # scale (float to multiply amounts by)
    return


make_vegetarian('https://www.allrecipes.com/recipe/172060/hummus-and-prosciutto-wrap/')

test_url = 'https://www.allrecipes.com/recipe/150273/spicy-pimento-cheese-sandwiches-with-avocado-and-bacon/'

recipe_data = get_recipe_json.get_recipe_json(test_url)

make_healthy(recipe_data)