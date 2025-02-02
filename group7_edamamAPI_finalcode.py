import os
import csv
import requests
from dotenv import load_dotenv

load_dotenv()


def recipe_search1(ingredient1, ingredient2, ingredient3): #for no dietary restrictions
    # Register to get an APP ID and key https://developer.edamam.com/
    app_id = os.getenv('APP_ID')
    app_key = os.getenv('APP_KEY')
    result = requests.get('https://api.edamam.com/search?q={},{},{}&app_id={}&app_key={}'.format(ingredient1, ingredient2, ingredient3, app_id, app_key))
    data = result.json()
    return data['hits']

def recipe_search2(ingredient1, ingredient2, ingredient3, restriction): #for dietary restrictions, includes the label 'health' in url
    # Register to get an APP ID and key https://developer.edamam.com/
    app_id = os.getenv('APP_ID')
    app_key = os.getenv('APP_KEY')
    result = requests.get('https://api.edamam.com/search?q={},{},{}&health={}&app_id={}&app_key={}'.format(ingredient1, ingredient2, ingredient3, restriction, app_id, app_key))
    data = result.json()
    return data['hits']


# Function to get nutritional information for a single ingredient
def ingredient_nutrition(ingredient):
    app_id = os.getenv('NUTRIENT_ID')
    app_key = os.getenv('NUTRIENT_KEY')
    result = requests.get(
        'https://api.edamam.com/api/nutrition-data?app_id={}&app_key={}&nutrition-type=logging&ingr={}'.format(app_id,
                                                                                                               app_key,
                                                                                                               ingredient)
    )
    data = result.json()
    return data


def run():

    field_names = ['label', 'uri', 'ingredients', 'calories']
    with open('recipies.csv', 'w+', newline='') as recipes_csv:
        spreadsheet = csv.DictWriter(recipes_csv, fieldnames=field_names)
        spreadsheet.writeheader()

        ingredient1 = input('Enter your primary ingredient: ')  # ingredient search is the basis of the project

        # Check if the user wants nutritional information for the first ingredient
        nutrition_yn = input("Would you like to get nutritional information for {}? Yes/No ".format(ingredient1)).lower()
        if nutrition_yn == 'yes':
            nutrition_data = ingredient_nutrition(ingredient1)
            print('Nutritional Information for {}:'.format(ingredient1))
            print(nutrition_data)
            print('')

        second_ingredient = input("Add additional ingredient? Yes/No ").lower()
        if second_ingredient == 'no':
            ingredient2 = ''
            ingredient3 = ''
        elif second_ingredient == 'yes':
            ingredient2 = input('Enter your secondary ingredient: ')

            # Check if the user wants nutritional information for the second ingredient
            nutrition_yn2 = input(
                "Would you like to get nutritional information for {}? Yes/No ".format(ingredient2)).lower()
            if nutrition_yn2 == 'yes':
                nutrition_data2 = ingredient_nutrition(ingredient2)
                print('Nutritional Information for {}:'.format(ingredient2))
                print(nutrition_data2)
                print('')

            third_ingredient = input("Add final additional ingredient? Yes/No ").lower()
            if third_ingredient == 'no':
                ingredient3 = ''
            elif third_ingredient == 'yes':
                ingredient3 = input('Enter your third ingredient: ')

                # Check if the user wants nutritional information for the third ingredient
                nutrition_yn3 = input(
                    "Would you like to get nutritional information for {}? Yes/No ".format(ingredient3)).lower()
                if nutrition_yn3 == 'yes':
                    nutrition_data3 = ingredient_nutrition(ingredient3)
                    print('Nutritional Information for {}:'.format(ingredient3))
                    print(nutrition_data3)
                    print('')
            else:
                print('Invalid answer, please restart.')
                exit()
        else:
            print('Invalid answer, please restart.')
            exit()

        dietary_restriction = [
            "alcohol-free",
            "dairy-free",
            "gluten-free",
            "kosher",
            "peanut-free",
            "pork-free",
            "shellfish-free",
            "vegan",
            "vegetarian"
        ]
        print('')
        print(dietary_restriction)
        print('')

        # Ask the user if they have dietary restrictions
        diet_yn = input('Do you have any dietary restrictions mentioned on the above list? Yes/No ').lower()
        if diet_yn == 'yes':
            restriction = input('Please specify which one. Enter answer exactly as listed. ').lower()
            if restriction in dietary_restriction:
                print('Restriction: {}'.format(restriction))
                results = recipe_search2(ingredient1, ingredient2, ingredient3, restriction)
                if not results:
                    print('')
                    print('No matches.')
                else:
                    for result in results:
                        recipe = result['recipe']
                        print('')
                        print(recipe['label'])
                        print(recipe['uri'])
                        print()
            else:
                print('Invalid answer, please restart.')
                exit()
        elif diet_yn == 'no':
            print('')
            results = recipe_search1(ingredient1, ingredient2, ingredient3)
            if not results:
                print('')
                print('No matches.')
            else:
                for result in results:
                    recipe = result['recipe']
                    print('')
                    print(recipe['label'])
                    print(recipe['uri'])
                    print()
                    spreadsheet.writerow({
                        'label': recipe['label'],
                        'uri': recipe['uri'],
                        'ingredients': recipe['ingredients'],
                    })
        else:
            print('Invalid answer, please restart.')
            exit()


run()