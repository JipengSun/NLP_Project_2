import nltk
import steps_parser
import get_recipe_json

def make_healthy(recipe_data,steps_data):
    #replace unhealthy foods with healthy alternatives
    #replace frying with alternative method
    [unhealthy_ingredient_data,healthy_ingredient_data,category_reason] = steps_parser.build_ingredient_type_structure()
    #print(recipe_data['ingredients'])
    
    # Overall analysis of ingredients
    #print(len(category_reason.keys()))
    ingredients_type = {}
    get_ingredients_types(ingredients_type,recipe_data,healthy_ingredient_data,unhealthy_ingredient_data)
    #print(ingredients_type)
    get_overall_analysis(ingredients_type,category_reason)
    print_analysis_text(ingredients_type,category_reason)
    

    
    #print(steps_data)


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

def print_analysis_text(ingredients_type,category_reason):
    print("Your original recipe contains following types of ingredients:")
    print(" ")
    for key, values in ingredients_type.items():
        print(key+':')
        for value in values:
            print_ingredient(value)
        print(' ')
    print("Based on your recipe, we would like to give you following health suggestions:")
    print(" ")
    index = 1
    for key, values in ingredients_type.items():
        print(str(index)+'. '+category_reason[key])
        index += 1

def print_ingredient(ing_dict):
    if ing_dict['unit'] == '':
        print('\t'+ing_dict['name'])
    else:
        print('\t'+str(ing_dict['quantity']) + ' ' + ing_dict['unit']+ ' ' + ing_dict['name'])

test_url = 'https://www.allrecipes.com/recipe/150273/spicy-pimento-cheese-sandwiches-with-avocado-and-bacon/'
#test_url = 'https://www.allrecipes.com/recipe/143809/best-steak-marinade-in-existence/'
#test_url = 'https://www.allrecipes.com/recipe/276206/stuffed-turkey-meatloaf/'

recipe_data = get_recipe_json.get_recipe_json(test_url)
steps_data = steps_parser.parse_step_data(recipe_data)

make_healthy(recipe_data,steps_data)

#print(recipe_data)