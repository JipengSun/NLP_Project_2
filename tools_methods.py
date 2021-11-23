
import pandas as pd
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
import get_recipe_json
import itertools

data = get_recipe_json.get_recipe_json("https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/")
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
#         "Heat oil in a skillet over medium-high heat. Stir in onion and lemon juice. Cook until onion is tender. Mix in turkey, season with curry powder and continue cooking until heated through.",
#         "Remove from heat. Stir in apple. Stuff pitas with the mixture. Drizzle with yogurt to serve."
#     ]
# }


method1=data["steps"]
#print(method1)
data = pd.DataFrame(method1)
list_o=[]
for s in method1:
    a_list = nltk.tokenize.sent_tokenize(s)
    list_o.extend(a_list)
    
# data = data.astype(str)
# first_words = data.apply(lambda x: x.str.split().str[0])
    #first_words=[word_tokenize(sent) for sent in a_list]
    #print (a_list)
final_list1=[]
for v in list_o:
    text1=nltk.word_tokenize(v)
    #print(text1)
    pos_tagged = nltk.pos_tag(text1)
    #print(pos_tagged)
    verbs = filter(lambda x:x[1]=='NNP' or x[1]=='VB',pos_tagged)
    final = list(verbs)
    final_1=[]
    for j in final:
        final_1.append(j[0])
    final_list1.extend(final_1)


    #final_list=list(itertools.chain(final_1))
    #print(final_list1)    
    #print(list(verbs))

# for f in final_1:
#     final_list1.extend(f)
print(set(final_list1))


    

    