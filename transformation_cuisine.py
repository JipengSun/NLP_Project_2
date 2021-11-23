
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

print("The Original Recipe is: ")
print(data)
text_recipe_name = data['name']
dict_ = {
    "sausage":"tofu",
    "ground beef":"chicken",
    "beef":"chicken",
    "italian seasoning":"masala",
    "italian seasoned":"masala",
    "parsley":"corriander",
    "meat sauce":"schezwan sauce",
    "bacon":"chicken",
    "turkey":"chicken",
    "worcestershire":"schezwan sauce",
    "dijon":"mustard paste",
    "brown sugar":"sugar",
    "olive oil":"groundnut oil"
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



print(data['ingredients'])
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