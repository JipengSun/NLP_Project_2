
import pandas as pd
import nltk
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
import itertools
import spacy
import get_recipe_json
nlp=spacy.load('en_core_web_sm')

def get_tools_recipe(url):

    tools_dict=['teaspoon','cup','tablespoon','teaspoons','tablespoons','oven','skillet','bowl','pan','cups','saucepans','saucepan','sheet','spatula','dish','cloth','glass','glasses','plate','knife','fork']


    data = get_recipe_json.get_recipe_json(url)


    text=data["steps"]
    ingredients=data["ingredients"]
    final_tools_list=[]
    final_tools_list1=[]
    for i,val in enumerate(ingredients):
        if val["unit"] in tools_dict:
            final_tools_list.append(val["unit"])

    for i2,val2 in enumerate(text):
  
        S1 = set(val2.split(", "))
 
        S1 = ' '.join(S1)
        S1 = set(S1.split("."))
 
        S1 = ' '.join(S1)
        S1 = set(S1.split())

  
        S2 = set(tools_dict)


        if len(S1.intersection(S2))>0:
            final_tools_list1.append(list(S1.intersection(S2)))
    flat_list = [item for sublist in final_tools_list1 for item in sublist]

    final_ = list(set(final_tools_list + flat_list))
    list_dum=[]
    for f,val3 in enumerate(final_):
        for j in range(len(final_)):
            if j!=f:
                if val3 in final_[j] and val3 not in list_dum:
                    list_dum.append(val3)
        



    print("The cooking tools/utensils used in the recipe are:")
    print(list(set(final_)^set(list_dum)))





    

    