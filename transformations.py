#tranformations
import json
import nltk
from nltk.probability import DictionaryConditionalProbDist
import get_recipe_json
import steps_parser
import healthy_transformation
import transformation_cuisine
import string
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'): 
        command = 'cls'
    os.system(command)

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
    clearConsole()
    meats_dict = ['chicken', 'beef', 'pork', 'lamb', 'fish', 'salmon', 'Prosciutto']
    meat_alternatives = ['Tofu', 'Seitan']
    #get type of alternative

    print("\nWhat kind of meat alternative would you like? (enter number)\n")
    for alt in range(len(meat_alternatives)):
        print(str(alt) + ": " + meat_alternatives[alt] + "\n")

    meat_alt = input_check('num', 2)
    meat_alt = meat_alternatives[int(meat_alt)]

    #get recipe
    recipe_data_ = get_recipe_json.get_recipe_json(recipe_url)
    steps_data = steps_parser.parse_step_data(recipe_data_)

    



    #fix name
    recipe_name = recipe_data_['name']
    removed_meats = []
    removed_meat = []
    for meat in meats_dict:
        recipe_name = recipe_name.replace(meat, meat_alt)
        removed_meats.append(meat)
    recipe_data_['name'] = recipe_name

    #fix ingredients
    for ingredient in recipe_data_['ingredients']:
        for meat in removed_meats:
            if meat.lower() in ingredient['name'].lower():
                ingredient['name'] = meat_alt
                #what to do with units?
                ingredient['unit'] = ''
                ingredient['quantity'] = ''
                removed_meat.append(meat)


    
    #fix steps
    # print(steps_data)
    for step in range(len(steps_data)):
        for meat in removed_meats:
    
            if meat.lower() in steps_data[step]['original_text'].lower():
                steps_data[step]['original_text'] = steps_data[step]['original_text'].lower().replace(meat.lower(), meat_alt)

    ##prints
    print("Changes: \n")
    for rm in removed_meat:
        print("Removed " + rm + ".")
    print("Added " + meat_alt + ".\n\n")
    print("Ingredients: \n")
    for ingredient in recipe_data_['ingredients']:
        print(ingredient['name'])
    print("\n\n")
    steps_parser.print_steps_data(steps_data)

    
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

    steps_data = steps_parser.parse_step_data(recipe_data)
    healthy_transformation.make_healthy(recipe_data,steps_data)
        


def make_indian(url):
    transformation_cuisine.get_indian_recipe(url)
    #remove all spices, replace with indian spices
    #[remove certain meats, replace with others?]

    #dictionary

    #no beef, use spices (red chile powder [paste], curry powder, masala)
    #mostly eat chicken

    return

def make_kosher(recipe_url, dairy_free = 0):
    clearConsole()
    changes = []
    unkosher = ['pork', "prosciutto", "shrimp", 'lobster', 'crab']
    meats_dict = ['chicken', 'beef', 'lamb', 'fish', 'salmon']
    dairy_dict = ['cheese', 'milk', 'cream']
    meat_alternatives = ['Tofu', 'Seitan']
    #get type of alternative
    if dairy_free:
        dish = 1
    else:
        print("Do you want this dish to be 0: meat, 1: dairy, or 2: parve?\n")
        dish = input_check('num', 2)
        dish = int(dish)

    recipe_data = get_recipe_json.get_recipe_json(recipe_url)
    steps_data = steps_parser.parse_step_data(recipe_data)


    recipe_name = recipe_data['name']
    
    if dish < 3:
        #if meat
        removed_unkosh = []
        replaced = False

        for thing in range(len(unkosher)):
            if unkosher[thing] in recipe_name.lower():
                if not replaced:
                    
                    if dish == 0:
                        print("What kind of meat do you want?\n")
                        for meat in range(len(meats_dict)):
                            print(str(meat) + ": " + meats_dict[meat])
                        meat_alt = input_check('num', 4)
                        meat_alt = meats_dict[int(meat_alt)]
                    else:
                        print("What kind of meat substitute do you want?\n")
                        for alt in range(len(meat_alternatives)):
                            print(str(alt)+ ": " + meat_alternatives[alt])
                        meat_alt = input_check('num', 1)
                        meat_alt = meat_alternatives[int(meat_alt)]
                    replaced = True
                removed_unkosh.append(unkosher[thing])

                #log change:
                changes.append("Replaced " + unkosher[thing] + " with " + meat_alt + ".")

             
                #fix title
                recipe_name = recipe_name.lower().replace(unkosher[thing], meat_alt)
            recipe_data['name'] = string.capwords(recipe_name)

            #fix ingredients
            for ingredient in recipe_data['ingredients']:
                for unkosh in removed_unkosh:
                    if unkosh.lower() in ingredient['name'].lower():
                        ingredient['name'] = meat_alt
                        #what to do with units?
                        ingredient['unit'] = ''                            
                        ingredient['quantity'] = ''
                
                if dish == 0 or dish == 2:
                #remove dairy
                    for d in dairy_dict:
                        if d.lower() in ingredient['name'].lower() and "non-dairy" not in ingredient['name'].lower():
                            changes.append("Replaced " + ingredient['name'] + " with optional non-dairy " + ingredient['name'] + ".")
                            ingredient['name'] = "non-dairy " + ingredient['name'] + " (optional)"
                            

                            

            #fix step
        print("Changes: \n")
        for change in changes:
            print(change)



    #get recipe
    



    #fix name
        recipe_name = recipe_data['name']
        removed_meats = []
        for meat in meats_dict:
            recipe_name = recipe_name.replace(meat, meat_alt)
            removed_meats.append(meat)
        recipe_data['name'] = recipe_name


    print(removed_unkosh)
    for step in range(len(steps_data)):
        for meat in removed_unkosh:
    
            if meat.lower() in steps_data[step]['original_text'].lower():
                steps_data[step]['original_text'] = steps_data[step]['original_text'].lower().replace(meat.lower(), meat_alt)
   
 
    print("\n\nIngredients: \n")
    for ingredient in recipe_data['ingredients']:
        print(ingredient['name'])
    print("\n\n")
    steps_parser.print_steps_data(steps_data)

    return



def make_gluten_free(recipe):
    return



### optional
def scale_recipe(recipe_data, scale):
    # scale (float to multiply amounts by)
    steps_data = steps_parser.parse_step_data(recipe_data)
    new_steps = []
    for step_data in steps_data:
        new_step = step_data
        for i,ingredient in enumerate(new_step['ingredients']):
            if new_step['ingredients'][i]['quantity']!='':
                new_step['ingredients'][i]['quantity'] = new_step['ingredients'][i]['quantity']*scale
        if len(new_step['cooking_time'])!=0:
            for i, cooking_time in enumerate(new_step['cooking_time']):
                new_step['cooking_time'][i] = new_step['cooking_time'][i]*scale*0.5

        new_steps.append(new_step)
    steps_parser.print_steps_data(new_steps)


    return



# make_kosher('https://www.allrecipes.com/recipe/172060/hummus-and-prosciutto-wrap/')
# make_kosher('https://www.allrecipes.com/recipe/172060/hummus-and-prosciutto-wrap/')
# make_vegetarian('https://www.allrecipes.com/recipe/172060/hummus-and-prosciutto-wrap/')

test_url = 'https://www.allrecipes.com/recipe/150273/spicy-pimento-cheese-sandwiches-with-avocado-and-bacon/'

recipe_data = get_recipe_json.get_recipe_json(test_url)

scale_recipe(recipe_data,5)

# make_healthy(recipe_data)

# scale_recipe(recipe_data)

