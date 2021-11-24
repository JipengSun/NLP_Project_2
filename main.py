import transformations
import get_recipe_json

def main():
    while True:
        transformations.clearConsole()
        transformations_list = ['Make Vegetarian', "Make Healthy", "Make Kosher", "Make Indian-style (cuisine)", "Scale Recipe"]
        print("What is the url for your recipe?")
        url = input("> ")
        print("\nWhat kind of transformation would you like to apply to your recipe? \n(enter number)\n")

        for t in range(len(transformations_list)):
            print(str(t) + ": " +transformations_list[t])
        print("\n")

        chosen_transformation = transformations.input_check('num', 4)
        chosen_transformation = int(chosen_transformation)

        if chosen_transformation == 0:
            transformations.make_vegetarian(url)
        elif chosen_transformation == 1:
            recipe_data= get_recipe_json.get_recipe_json(url)
            transformations.make_healthy(recipe_data)
        elif chosen_transformation == 2:
            transformations.make_kosher(url)
        elif chosen_transformation == 3:
            transformations.make_indian(url)
        else:
            print("By what factor would you like to scale the recipe?")
            s = input("> ")
            s = int(s)
            recipe_data= get_recipe_json.get_recipe_json(url)
            transformations.scale_recipe(recipe_data, s)
        

        print("\n\nPerform another transformation? (1 for Yes, 0 for No)")
        again = transformations.input_check('num', 1)
        if not int(again):
            break
    
    

main()