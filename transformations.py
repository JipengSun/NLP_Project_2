#tranformations
import json
import nltk
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

    category_reason = {
        "trans_fat":"The original recipe contains too much trans-fat, which may add your chance to get inflammation.",
        "saturated_fat":"The original recipe contains saturated fat, which may cause artery blockage.",
        "massive_sugar":"The massive amount of added sugar may higher the chance of obesity",
        "salt":"Excessive sodium consumption is the key negetive factor of longevity.",
        "vegetables":"The original recipe doesn't contain vegetables which provides you essential Vitamins and fiber, consider adding some vegetables in your recipe",
        "fruit":"There is no fruit in your recipe but that is common, don't forget to eat some fruits after the meal!",
        "grains":"Grains are naturally high in fiber, helping you feel full and satisfied — which makes it easier to maintain a healthy body weight.",
        "protein":"The original recipe doesn't contain enough protein which is helpful for muscle gain and health."
    }
    massive_sugar = ['ice cream','candy','pastries','cookies','soda','fruit juices','canned fruit','processed meat','breakfast cereals','ketchup','beet sugar',\
        'blackstrap molasses','brown sugar','buttered syrup','cane juice crystals','cane sugar','caramel','carob syrup','castor sugar',\
            'coconut sugar','powdered sugar','date sugar','demerara sugar','Florida crystals','fruit juice','fruit juice concentrate','golden sugar',\
                'golden syrup','grape sugar','honey','icing sugar','invert sugar','maple syrup','molasses','muscovado sugar','panela sugar','rapadura',\
                    'raw sugar','refiner’s syrup','sorghum syrup','sucanat','treacle sugar','turbinado sugar','yellow sugar']

    unhealthy_oil = ['soybean oil','corn oil','cottonseed oil','sunflower oil','peanut oil','sesame oil','rice bran oil','flaxseed oil']
    trans_fat = ['fried food','chips','creamer','margarine']+unhealthy_oil

    red_meat = ['beef','lamb','mutton','pork','veal','venison','goat']
    processed_meat = ['sausage','bacon','ham','deli meats','salami','pâtés','canned meat','corned beef','luncheon meats','prosciutto']
    cheese = ['cheese','roquefort','camembert','cotija','chèvre','feta','mozzarella','emmental','cheddar','gouda','taleggio','parmigiano-reggiano','manchego','monterey jack']
    saturated_fat = ['coconut oil','whole milk'] + cheese + red_meat + processed_meat
    salt = ['salt']

    unhealthy_ingredient_data = {
        "massive_sugar":massive_sugar,
        "trans_fat":trans_fat,
        "saturated_fat":saturated_fat,
        "salt" : salt
    }


    vegetables = []
    with open('vegetable_list.txt') as f:
        line = f.readline()
        while line:
            line = f.readline()
            vegetables.append(line.strip().lower())
    #print(vegetables)
    fruits = []
    with open('fruit_list.txt') as f:
        line = f.readline()
        while line:
            line = f.readline()
            fruits.append(line.strip().lower())
    #print(fruits)
    grains = ['quinoa','corn','millet','brown rice']
    healthy_oil = ['olive oil','canola oil','aocado oil','walnut oil']
    white_meat = ['chicken','turkey','duck','goose','game birds','rabbit','pheasant']
    fish_meat = ['salmon','cod','herring','mahi-mahi','mackerel','perch','rainbow trout','sardines','striped bass','tuna','alaskan pollock','char']
    soy_products = []
    with open('soy_product_list.txt') as f:
        line = f.readline()
        while line:
            line = f.readline()
            soy_products.append(line.strip().lower())
    #print(soy_products)

    legume_list = []
    with open('legume_list.txt') as f:
        line = f.readline()
        while line:
            line = f.readline()
            legume_list.append(line.strip().lower())
    #print(legume_list)

    protein = ['egg']+legume_list+soy_products+red_meat+white_meat+fish_meat

    healthy_ingredient_data = {
        'vegetables':vegetables,
        'fruits':fruits,
        'grains':grains,
        'protein':protein,
        'healthy_oil':healthy_oil,
        'white_meat':white_meat,
        'fish_meat':fish_meat
    }

    for step in recipe_data['steps']:
        a = nltk.word_tokenize(step)
        #print(a)
        
        


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