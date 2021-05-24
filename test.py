import os
import unittest
import sys
import requests
import spoon

# from ingeredients import sum
API_KEY = os.getenv('SPOON_API_KEY')

class TestMethods(unittest.TestCase):
    # test API KEY 
    def test_api_key(self):
    	self.assertIsNotNone(API_KEY, "API Key Not Found")

    def test_spoon_ingredients(self): 
    	s = spoon.findRecipe("Potato")
    	self.assertEqual(s, "success", "Unable to access spoon API")
    	

    # def test_api(self):
    # 	request_recipes = 'https://api.spoonacular.com/recipes/findByIngredients?ingredients=potato&apiKey=' + API_KEY
    # 	try: 
    # 		response_recipes = requests.get(request_recipes)
    # 		self.assertEqual(response_recipes.status_code, 200, "Unable to access spoon API")
    # 	except: 
    # 		print("Error")
    # 		self.assertTrue(False, "Unable to access spoon API")


if __name__ == '__main__':
    unittest.main()