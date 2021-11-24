import pandas as pd
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
import get_recipe_json
import itertools


def get_methods_recipe(url):
    data = get_recipe_json.get_recipe_json(url)



    method1=data["steps"]
    data = pd.DataFrame(method1)
    list_o=[]
    for s in method1:
        a_list = nltk.tokenize.sent_tokenize(s)
        list_o.extend(a_list)
    

    final_list1=[]
    for v in list_o:
        text1=nltk.word_tokenize(v)
        pos_tagged = nltk.pos_tag(text1)
        verbs = filter(lambda x:x[1]=='NNP' or x[1]=='VB',pos_tagged)
        final = list(verbs)
        final_1=[]
        for j in final:
            final_1.append(j[0])
        final_list1.extend(final_1)



    print("The cooking methods used in the Recipe are:")
    print(set(final_list1))


    

    