
import pandas as pd
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
import itertools
import spacy

from fractions import Fraction as frac
import get_recipe_json
nlp=spacy.load('en_core_web_sm')

data = get_recipe_json.get_recipe_json("https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/")
#data = get_recipe_json.get_recipe_json("https://www.allrecipes.com/recipe/276206/stuffed-turkey-meatloaf/")

print("The Original Recipe is: ")
print(data)


ingredients_l=[]

for i,ingredient in enumerate(data['ingredients']):
    data['ingredients'][i]['quantity'] = ingredient['quantity'] * 2
for i,ingredient in enumerate(data['ingredients']):
    ingredients_l.append(str(data['ingredients'][i]['quantity'])+" "+str(data['ingredients'][i]['unit'])+" "+data['ingredients'][i]['name'])


print("Transformed Recipe for Doubling the amount of quantities")

print("\nThe Transformed Ingredients are: ")
#print(data['ingredients'])
print(ingredients_l)

text=data["steps"]

        


dummy_list=[]
time_arr =['minutes','minutes.','hours','hour','degrees','to']

for i1,t in enumerate(text):
    print("Original Recipe Step: ",t)
    t_list = t.split()
    l = []
    for i2,t1 in enumerate(t_list):
        next=t_list[i2]
        if i2+1<len(t_list):
            next=t_list[i2+1]
        try:
            app = float(frac(t1))
            try:
                m=float(frac(t_list[i2+1]))
                t_list[i2+1]=""
                if i2+1<len(t_list):
                    next=t_list[i2+2]
                app= app+m
            except ValueError:
                pass  
            if next in time_arr:  

                t_list[i2]=str(app)
            else:
                t_list[i2]=str(app*2)

        except ValueError:
            pass
    text[i1]= ' '.join(t_list)

    #print(l)
print("\nThe Transformed recipe steps are:")
print(text)






        








    

    