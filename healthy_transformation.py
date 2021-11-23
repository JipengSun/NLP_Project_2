import steps_parser
import get_recipe_json

def make_healthy(recipe_data,steps_data):
    #replace unhealthy foods with healthy alternatives
    #replace frying with alternative method
    [unhealthy_ingredient_data,healthy_ingredient_data,category_reason] = steps_parser.build_ingredient_type_structure()
    
    '''
    step_tokens = nltk.word_tokenize(step)
    for token in step_tokens:
        find_token_in_dict(token,unhealthy_ingredient_data)
        find_token_in_dict(token,healthy_ingredient_data)
    '''
    #print(steps_data)


#test_url = 'https://www.allrecipes.com/recipe/150273/spicy-pimento-cheese-sandwiches-with-avocado-and-bacon/'
#test_url = 'https://www.allrecipes.com/recipe/143809/best-steak-marinade-in-existence/'
test_url = 'https://www.allrecipes.com/recipe/276206/stuffed-turkey-meatloaf/'

recipe_data = get_recipe_json.get_recipe_json(test_url)
steps_data = steps_parser.parse_step_data(recipe_data)

make_healthy(recipe_data,steps_data)

print(recipe_data)