#!/usr/bin/python
import requests
import json
import os
#termcolor can print console output in various colors. 
from termcolor import colored


#Set API Key - export SPOON_API_KEY = <API_KEY>
API_KEY = os.getenv('SPOON_API_KEY')


#The input parameter ingredients will 
def findRecipe(ingrs):
    # list of ingredients
    Listingredient = list()

    #We cannot proceed if no API key was found
    if API_KEY is None:
        print('\n\n************************************************')
        print('******* API KEY NOT FOUND - EXITING ************')
        print('************************************************\n\n')
        quit()
        

    
    if ingrs is None: 
        #Ask for ingredients from command prompt
        input_ingred = input("Enter a list of ingredients separated by space ")
        Listingredient  = input_ingred.split()
        #The ingeredient list accepted by API is in format ingr1,+ingr2,+
        Listingredient = ",+".join(Listingredient)
    else: 
        Listingredient = ingrs

    # Spponacular find by ingredients API
    request_recipes = 'https://api.spoonacular.com/recipes/findByIngredients?ingredients=' + Listingredient + '&apiKey=' + API_KEY

    try: 
        response_recipes = requests.get(request_recipes)
    except: 
        print('\n\n\n**********************************************************************************************')
        print('******* Oops, something went wrong. ************************************************************')
        print('******* Please check your API Key or try again later ***********************************************')
        print('************************************************************************************************\n\n\n')
        quit()

    # Check status code
    if response_recipes.status_code != 200:
        print('\n**********************************************************************************************')
        print('******* Oops, something went wrong. ************************************************************')
        print('******* Please check your API or try again later ***********************************************')
        print('************************************************************************************************\n\n\n')
        quit()

    recipes = response_recipes.json()

    result = dict()
    print('\n**********************************************************************************************')
    print('******** We found below popular recipes with your ingredients. *********************************')
    print('******** If there were any missing ingeredients then they will be mentioned in red color********')
    print('************************************************************************************************')
    for recipe in recipes:
        print('\n')
        title = recipe['title']
        print(colored(title, 'green'))
        missedIngredients = list(recipe['missedIngredients'])
        if not missedIngredients:
            pass
        # print(missedIngredients)
        for mi in missedIngredients:
            name = mi['name']
            print(colored(name,'red'))

    return "success"

if __name__ == '__main__':
    findRecipe(None)