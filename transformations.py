#tranformations

from nltk.probability import DictionaryConditionalProbDist
import get_recipe_json


def make_vegetarian(recipe_url):
    #replace meats with vegetarian alternatives
    meats_dict = ['chicken', 'beef', 'pork', 'lamb', 'fish', 'salmon']
    meat_alternatives = ['tofu', 'seitan', 'beans', 'lentils']
    #get recipe
    r = get_recipe_json.get_recipe_json(recipe_url)
    recipe_json = 'raw_recipe.json'
    print(type(recipe_json))


    #go through ingredients, replace meats with selected alternative [maybe]
    #go through steps, replace meats with selected alternatives
    #look at quantities and maybe change if it says "1 piece of chicken"

    #what if it says 'chicken breast'? use dependency parser? to replace both at the same time
    #print what the changes we made were - maybe call function to print out original recipe
    #print all transformed steps

    return recipe_json

def make_healthy(recipe):
    #replace unhealthy foods with healthy alternatives
    #replace frying with alternative method
    
    return 

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