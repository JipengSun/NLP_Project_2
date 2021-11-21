import nltk
import get_recipe_json

def make_healthy(recipe_data):
    #replace unhealthy foods with healthy alternatives
    #replace frying with alternative method
    [unhealthy_ingredient_data,healthy_ingredient_data,category_reason] = build_ingredient_type_structure()

    for step in recipe_data['steps']:
        find_ingredient(step,unhealthy_ingredient_data,category_reason)
        find_ingredient(step,healthy_ingredient_data,category_reason)
        '''
        step_tokens = nltk.word_tokenize(step)
        for token in step_tokens:
            find_token_in_dict(token,unhealthy_ingredient_data)
            find_token_in_dict(token,healthy_ingredient_data)
        '''
        

def find_token_in_dict(token,dict1):
    for key, values in dict1.items():
        if token in values:
            print(token)
            print(key)

def find_ingredient(sentence,type_dict,reason_dict):
    for key, values in type_dict.items():
        for value in values:
            if value != '' and value in sentence.lower():
                print(reason_dict[key])
                print(value)

def txt2list(filename, newlist):
    with open(filename) as f:
        line = f.readline()
        while line:
            line = f.readline()
            newlist.append(line.strip().lower())

def build_ingredient_type_structure():
    category_reason = {
        "trans_fat":"The original recipe contains too much trans-fat, which may add your chance to get inflammation.",
        "saturated_fat":"The original recipe contains saturated fat, which may cause artery blockage.",
        "massive_sugar":"The massive amount of added sugar may higher the chance of obesity",
        "salt":"Excessive sodium consumption is the key negetive factor of longevity.",
        "vegetables":"The original recipe doesn't contain vegetables which provides you essential Vitamins and fiber, consider adding some vegetables in your recipe",
        "fruits":"There is no fruit in your recipe but that is common, don't forget to eat some fruits after the meal!",
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
    txt2list('vegetable_list.txt',vegetables)

    fruits = []
    txt2list('fruit_list.txt',fruits)
    
    grains = ['quinoa','corn','millet','brown rice']
    healthy_oil = ['olive oil','canola oil','aocado oil','walnut oil']
    white_meat = ['chicken','turkey','duck','goose','game birds','rabbit','pheasant']
    fish_meat = ['salmon','cod','herring','mahi-mahi','mackerel','perch','rainbow trout','sardines','striped bass','tuna','alaskan pollock','char']

    soy_products = []
    txt2list('soy_product_list.txt',soy_products)

    legume_list = []
    txt2list('legume_list.txt',legume_list)

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

    return [unhealthy_ingredient_data,healthy_ingredient_data,category_reason]




test_url = 'https://www.allrecipes.com/recipe/150273/spicy-pimento-cheese-sandwiches-with-avocado-and-bacon/'

recipe_data = get_recipe_json.get_recipe_json(test_url)

make_healthy(recipe_data)
