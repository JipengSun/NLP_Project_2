
import pandas as pd
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
import itertools
import spacy
import get_recipe_json
nlp=spacy.load('en_core_web_sm')

data = get_recipe_json.get_recipe_json("https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/")
#data = get_recipe_json.get_recipe_json("https://www.allrecipes.com/recipe/276206/stuffed-turkey-meatloaf/")

print(data)
text_recipe_name = data['name']
dict_ = {
    "sausage":"tofu",
    "ground beef":"chicken",
    "beef":"chicken",
    "italian seasoning":"masala",
    "parsley":"corriander",
    "meat sauce":"schezwan sauce",
    "bacon":"chicken"
}

mapping = dict_
for d in mapping:
    text_recipe_name = text_recipe_name.lower().replace(d,mapping[d])
    for i,ingredient in enumerate(data['ingredients']):
        #print("NAME",ingredient['name'])
        if d in ingredient['name'].lower():

            data['ingredients'][i]['name'] = ingredient['name'].lower().replace(d,mapping[d])

print(text_recipe_name)


# for ingredient in data['ingredients']:
#     if ingredient['name'].lower() in mapping:
#         ingredient['name'] = [w.lower().replace(ingredient,mapping[ingredient]) for w in data['ingredients']]
#         #what to do with units?
#         ingredient['unit'] = ''
#         ingredient['quantity'] = ''

print(data['ingredients'])
# data={
# 	"name": "Apple Curry Turkey Pita",
# 	"ingredients":[
#         {
#             "quantity":0.5,
#             "unit":"tablespoon",
#             "name":"salt"
#         },
#         {
#             "quantity":1,
#             "unit":"teaspoons",
#             "name":"paprika"
#         },
#         {
#             "quantity":0.5,
#             "unit":"pound",
#             "name":"cooked turkey, cut into chunks"
#         }
# 	],
#     "steps":[
#         "In a Dutch oven, cook sausage, ground beef, onion, and garlic over medium heat until well browned. Stir in crushed tomatoes, tomato paste, tomato sauce, and water. Season with sugar, basil, fennel seeds, Italian seasoning, 1 teaspoon salt, pepper, and 2 tablespoons parsley. Simmer, covered, for about 1 1/2 hours, stirring occasionally.",
#         "Bring a large pot of lightly salted water to a boil. Cook lasagna noodles in boiling water for 8 to 10 minutes. Drain noodles, and rinse with cold water. In a mixing bowl, combine ricotta cheese with egg, remaining parsley, and 1/2 teaspoon salt.",
#         "Preheat oven to 375 degrees F (190 degrees C).",
#         "To assemble, spread 1 1/2 cups of meat sauce in the bottom of a 9x13-inch baking dish. Arrange 6 noodles lengthwise over meat sauce. Spread with one half of the ricotta cheese mixture. Top with a third of mozzarella cheese slices. Spoon 1 1/2 cups meat sauce over mozzarella, and sprinkle with 1/4 cup Parmesan cheese. Repeat layers, and top with remaining mozzarella and Parmesan cheese. Cover with foil: to prevent sticking, either spray foil with cooking spray, or make sure the foil does not touch the cheese.",
#         "Bake in preheated oven for 25 minutes. Remove foil, and bake an additional 25 minutes. Cool for 15 minutes before serving."
#     ]
# }

text=data["steps"]
#text=str(text)
#split_ = text.split()




new_steps = []
for ing in mapping:
    text = [w.lower().replace(ing,mapping[ing]) for w in text]

    #new_steps.append(step.replace(ing,mapping[ing]))
        #print("MAP",mapping[ing],"TEXT",step.replace(ing,mapping[ing]))
    
print(text)

    
    # # transform raw step
    # for ing in mapping:
    #     if ing in step['raw_step']:
    #         step['raw_step'] = step['raw_step'].replace(ing, mapping[ing])
    #         # print(f'replacing {ing} with {mapping[ing]}')
    #     elif ing[-1] == 's' and ing[:-1] in step['raw_step']:
    #         step['raw_step'] = step['raw_step'].replace(ing[:-1], mapping[ing])
    #         # print(f'replacing {ing[:-1]} with {mapping[ing]}')

# def transform_cuisine_steps(recipe, cuisine):
#     '''
#     Transforms the steps in the recipe for the given cuisine
#     '''
#     mapping = generate_ingredient_mapping(recipe['ingredients'])
#     for step in recipe['steps']:
#         # transform ingredients in steps
#         new_ingredients = []
#         for ing in step['ingredients']:
#             if ing in mapping:
#                 new_ingredients.append(mapping[ing])
#         step['ingredients'] = new_ingredients
        
#         # transform raw step
#         for ing in mapping:
#             if ing in step['raw_step']:
#                 step['raw_step'] = step['raw_step'].replace(ing, mapping[ing])
#                 # print(f'replacing {ing} with {mapping[ing]}')
#             elif ing[-1] == 's' and ing[:-1] in step['raw_step']:
#                 step['raw_step'] = step['raw_step'].replace(ing[:-1], mapping[ing])
#                 # print(f'replacing {ing[:-1]} with {mapping[ing]}')
    
#     for ing in mapping:
#         if ing in recipe['title']:
#             recipe['title'] = recipe['title'].replace(ing, mapping[ing])
#     return False
# ingredients=data['ingredients']
# def generate_ingredient_mapping(ingredients):
#     '''
#     Generates the ingredient mapping for the recipe
#     '''
#     mapping = {}
#     for food_type in ingredients:
#         for ing in ingredients[food_type]:
#             mapping[ing['matched_word']] = ing['ingredient']
#     return mapping




    

    