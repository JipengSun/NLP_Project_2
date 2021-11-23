import nltk
import steps_parser
import get_recipe_json
from random import randrange

def make_healthy(recipe_data,steps_data):
    #replace unhealthy foods with healthy alternatives
    #replace frying with alternative method
    [unhealthy_ingredient_data,healthy_ingredient_data,category_reason,health_replacement_mapping] = steps_parser.build_ingredient_type_structure()
    #print(recipe_data['ingredients'])
    
    # Overall analysis of ingredients
    #print(len(category_reason.keys()))
    ingredients_type = {}
    get_ingredients_types(ingredients_type,recipe_data,healthy_ingredient_data,unhealthy_ingredient_data)
    #print(ingredients_type)
    get_overall_analysis(ingredients_type,category_reason)

    new_ingredients = []
    new_ingredients = print_overall_analysis_text(ingredients_type,category_reason,health_replacement_mapping,recipe_data)
    #print(new_ingredients)
    new_steps_data = construct_new_steps(steps_data,new_ingredients)

    print("The new transformed healthy recipe is as following:")
    print(" ")
    print(steps_parser.print_steps_data(new_steps_data))





def get_ingredients_types(ingredients_type,recipe_data,healthy_ingredient_data,unhealthy_ingredient_data):
    for ingredient in recipe_data['ingredients']:
        ingredient_tokens = nltk.word_tokenize(ingredient['name'])
        for key, value in healthy_ingredient_data.items():
            if ingredient['name'] in value or any(token in value for token in ingredient_tokens):
                if key in ingredients_type.keys():
                    ingredients_type[key].append(ingredient)
                else:
                    ingredients_type[key] = [ingredient]

        for key, value in unhealthy_ingredient_data.items():
            if ingredient['name'] in value or any(token in value for token in ingredient_tokens):
                if key in ingredients_type.keys():
                    ingredients_type[key].append(ingredient)
                else:
                    ingredients_type[key] = [ingredient]
    
    return ingredients_type

def get_overall_analysis(ingredients_type,category_reason):
    analysis_list = []
    for type in category_reason.keys():
        if type in ingredients_type.keys():
            analysis_list.append({type:category_reason[type]})
    return analysis_list

def print_overall_analysis_text(ingredients_type,category_reason,health_replacement,recipe_data):
    print("Your original recipe contains following types of ingredients:")
    print(" ")
    for key, values in ingredients_type.items():
        print(key+':')
        for value in values:
            print('\t'+ steps_parser.get_ingredient_str(value))
            #print_ingredient(value)
        print(' ')
    print("Based on your recipe, we would like to give you following health suggestions:")
    print(" ")
    index = 1
    for key, values in ingredients_type.items():
        print(str(index)+'. '+category_reason[key])
        index += 1
    print(" ")
    print('For your health, we make following changes to your original recipe:')
    print(" ")

    new_ingredients = []

    for key, values in ingredients_type.items():
        if key in health_replacement:
            for value in values:
                if 'amount_change' in health_replacement[key].keys():
                    ing_dict = {'quantity':value['quantity']*health_replacement[key]['amount_change'],
                    'unit':value['unit'],
                    'name':value['name']}
                    new_ingredients.append([value,ing_dict])
                    print('\t'+steps_parser.get_ingredient_str(value)+" ==> "+steps_parser.get_ingredient_str(ing_dict))
                else:
                    for k,v in health_replacement[key].items():
                        ing_dict = {'quantity':value['quantity'],'unit':value['unit'],'name':v[randrange(len(v))]}
                        new_ingredients.append([value,ing_dict])
                        print('\t'+steps_parser.get_ingredient_str(value)+" ==> "+steps_parser.get_ingredient_str(ing_dict))
    
    print(" ")
    return new_ingredients

def construct_new_steps(steps_data,new_ingredients):
    new_steps_data = []
    #print(steps_data)
    for step_data in steps_data:
        step_structure = {
        'original_text':'',
        'ingredients':[],
        'tools':[],
        'methods':[],
        'cooking_time':[]
        }
        new_step_data = []
        new_step_text = step_data['original_text']
        for ingredient_data in step_data['ingredients']:
            for replacement in new_ingredients:
                if replacement[0] == ingredient_data:
                    ingredient_data = replacement[1]
            new_step_data.append(ingredient_data)
            
        new_step_text = steps_parser.replace_words_in_str(new_ingredients,new_step_text)
        
        step_structure['original_text'] = new_step_text
        step_structure['ingredients'] = new_step_data
        step_structure['tools'] = step_data['tools']
        step_structure['methods'] = step_data['methods']
        step_structure['cooking_time'] = step_data['cooking_time']

        new_steps_data.append(step_structure)
    #print(new_steps_data)
    return new_steps_data



test_url = 'https://www.allrecipes.com/recipe/150273/spicy-pimento-cheese-sandwiches-with-avocado-and-bacon/'
#test_url = 'https://www.allrecipes.com/recipe/143809/best-steak-marinade-in-existence/'
#test_url = 'https://www.allrecipes.com/recipe/276206/stuffed-turkey-meatloaf/'

recipe_data = get_recipe_json.get_recipe_json(test_url)
steps_data = steps_parser.parse_step_data(recipe_data)

make_healthy(recipe_data,steps_data)

#print(recipe_data)