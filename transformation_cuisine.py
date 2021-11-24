
import pandas as pd
import nltk
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
import itertools
import spacy
import get_recipe_json
import tools_methods
import tools_methods_1
nlp=spacy.load('en_core_web_sm')


def get_indian_recipe(url):
    #data = get_recipe_json.get_recipe_json("https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/")
    #data = get_recipe_json.get_recipe_json("https://www.allrecipes.com/recipe/276206/stuffed-turkey-meatloaf/")
    data = get_recipe_json.get_recipe_json(url)


    print("The Original Recipe is: ")
    print(data)

    tools_methods_1.get_tools_recipe(url)

    tools_methods.get_methods_recipe(url)
    
    
    
    text_recipe_name = data['name']
    dict_ = {
        "pork sausage":"tofu",
        "chicken sausage":"tofu",
        "pork ribs":"chicken",
        "clams":"fish",
        "pecans":"almonds",
        "grits":"corn",
        "extra virgin olive oil":"vegetable oil",
        "extra-virgin olive oil":"vegetable oil",
        "virgin olive oil":"vegetable oil",
        "balsamic vinegar":"lemon juice",
        "pasta":"rice",
        "pasta sauce":"garlic chutney",
        "oregano":"marva leaves",
        "italian-seasoned":"garam masala",
        "romano cheese":"amul cheese",
        "spaghetti":"rice",
        "prosciutto":"chicken",
        "capers":"peas",
        "porcini mushrooms":"mushrooms",
        "basil":"mint",
        "italian cheese":"amul cheese",
        "rabbit" : "eggs",
        "rosemary leaves":"marva leaves",
        "dipping sauce":"garlic chutney",
        "chipotle peppers":"green peppers",
        "pancetta":"chicken",
        "celery":"green onion",
        "tarragon":"mint",
        "italian":"indian",
        "spanish":"indian",
        "manicotti pasta":"rice",
        "marsala wine":"lemon juice",
        "sherry":"garlic chutney",
        "wine sherry":"lemon juice",
        "cayenne pepper":"green pepper",
        "fillets cod fillets": "fish",
        "brandy":"tomato puree",
        "bottle dry red wine":"lemon juice",
        "white wine":"lemon juice",
        "sofrito":"onions",
        "jamón ibérico":"chicken",
        "jamon iberico":"chicken",
        "sherry vinegar":"lemon juice",
        "olives":"peas",
        "cod fish":"fish",
        "red wine":"lemon juice",
        "fettuccine pasta":"rice",
        "tortillas":"rotis",
        "parmesan cheese":"amul cheese",
        "shrimp":"fish",
        "kale":"cabbage",
        "whipping cream":"curd",
        "noodles":"rice",
        "mozzarella cheese":"amul cheese",
        "chorizo":"chicken",
        "ricotta cheese":"amul cheese",
        "marinara sauce":"garlic chutney",
        "rice vinegar":"lemon juice",
        "mirin":"honey",
        "miso paste":"garlic chutney",
        "sesame oil":"vegetable oil",
        "soba noodles":"rice",
        "monosodium glutamate":"maggie bhuna masala",
        "aji-no-moto":"maggie bhuna masala",
        "tenkasu":"bread crumps",
        "sake":"lemon juice",
        "sea bass":"fish",
        "canola oil":"vegetable oil",
        "nori seaweed":"cabbage",
        "avocado":"almond",
        "crabmeat":"chicken",
        "sriracha hot sauce":"chilly garlic paste",
        "sriracha":"chilly garlic paste",
        "sriracha sauce":"chilly garlic paste",
        "nori":"cabbage",
        "dashi kombu":"mushrooms",
        "dashi granules":"mushrooms",
        "wakame":"spinach",
        "wakame seaweed":"spinach",
        "bonito flakes":"mushrooms",
        "shichimi togarashi":"maggie bhuna masala",
        "dark soy sauce":"chilly garlic paste",
        "shaoxing wine":"lemon juice",
        "oyster sauce":"mushroom sauce",
        "ground white pepper":"pepper",
        "red caviar":"peas",
        "wasabi paste":"ginger paste",    
        "veal":"chicken",
        "pesto":"mint chutney",
        "salsa":"garlic chutney",
        "mussels":"prawns",
        "baby squid":"fish",
        "asturian fabada":"chickpeas",
        "lima beans":"chickpeas",
        "nutmeg":"almonds",
        "cheese tortellini":"cheese cubes",
        "broccoli":"cauliflower",
        "asparagus":"spinach",
        "italian herb seasoning":"garam masala",
        "italian-style":"indian style",
        "collard greens":"spinach",
        "pumpkin":"potatoes",
        "turkey breast":"chicken",
        "shallot":"onions",
        "brussels sprouts":"peas",
        "prime rib roast":"wheat bread",
        "margarine":"butter",
        "soy sauce":"vegetable curry",
        "ground beef":"chicken",
        "beef":"chicken",
        "italian seasoning":"masala",
        "italian seasoned":"masala",
        "parsley":"corriander",
        "meat sauce":"schezwan sauce",
        "szechuan peppercorns":"corriander seeds",
        "bacon":"chicken",
        "turkey":"chicken",
        "worcestershire sauce":"schezwan sauce",
        "dijon":"mustard paste",
        "brown sugar":"sugar",
        "olive oil":"vegetable oil",
        "thai basil leaves":"mint",
        "thai":"indian",
        "black bean sauce":"schezwan sauce",
        "white soy sauce":"schezwan sauce",
        "gochujang":"chilly garlic paste",
        "chives":"onions",
        "dumpling wrappers":"paani poori",
        "beans":"chickpeas",
        "limes":"lemon juice",
        "jalapenos":"red chillies",
        "pumpkin seeds":"sesame seeds",
        "adobo sauce":"schezwan sauce",
        "enchilada sauce":"schezwan sauce",
        "hominy":"chickpeas",
        "chipotle sauce":"schezwan sauce",
        "masa harina":"wheat flour",
        "taco seasoning mix":"maggie bhuna masala",
        "chipotle chiles":"green chillies",
        "ancho chiles":"green chillies",
        "guajillo chiles":"green chillies",
        "sour cream":"curd",
        "cheddar cheese":"amul cheese",
        "fajita seasoning":"maggie bhuna masala",
        "monterey jack cheese":"amul cheese",
        "fish sauce":"schezwan sauce",
        "palm sugar":"sugar",
        "makham piak":"tamarind juice"

    }
    ingredients_l=[]
    mapping = dict_
    for d in mapping:
        text_recipe_name = text_recipe_name.lower().replace(d,mapping[d])
        for i,ingredient in enumerate(data['ingredients']):
            #print("NAME",ingredient['name'])
            if d in ingredient['name'].lower():

                data['ingredients'][i]['name'] = ingredient['name'].lower().replace(d,mapping[d])
    for i,ingredient in enumerate(data['ingredients']):
        ingredients_l.append(str(data['ingredients'][i]['quantity'])+" "+str(data['ingredients'][i]['unit'])+" "+data['ingredients'][i]['name'])

    print("\nThe transformed Recipe (Indian Cuisine) is:")
    print(text_recipe_name)



    #print(data['ingredients'])
    print("\nThe transformed ingredients are: ")
    print(ingredients_l)


    text=data["steps"]


    list_stepwise_ing=[]

    #INDIVIDUAL TRANSFORMED STEPS:

            



    original_rec=text
    #OVERALL TRANSFORMED STEPS
    new_steps = []
    for ing in mapping:
        text = [w.lower().replace(ing,mapping[ing]) for w in text]

    for ing in mapping:
        for i1,t in enumerate(text):
            #t_list = t.split()
            S1 = t.split(", ")
            S1 = ' '.join(S1)
            S1 = S1.split(".")
            S1 = ' '.join(S1)
            S1 = S1.split()
            if mapping[ing] in S1:
                print("The list of Transformed Ingredients are:")
                print({ing:mapping[ing]})


    print("\nThe transformed recipe steps are: ")
    print(text)


    for i1,t in enumerate(text):
        list_in = []
        dict_ = {}
        for i in data['ingredients']:
            #split_=i['name'].split()
            S1 = set(i['name'].split())
            S2 = set(t.split(", "))
    
            S2 = ' '.join(S2)
            S2 = S2.split(" ")
            #print(len(S1.intersection(S2)))
            if len(S1.intersection(S2))>0:
                list_in.append(i['name'])
        dict_["original_step"]=original_rec[i1]
        dict_["transformed_step"]=t
        dict_["ingredients"]=list_in
        list_stepwise_ing.append(dict_)
    print("\nThe step-wise transformation of the recipe is ")
    print(list_stepwise_ing)

# get_indian_recipe("https://www.allrecipes.com/recipe/276206/stuffed-turkey-meatloaf/")