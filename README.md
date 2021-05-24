# Find Recipes Using Spoonacular API

This Python application uses Spoonacular API to accept ingredients as user input from command line and then use them to search most popular recipes and display which ingredients are missing from the recipe.

## How it works
The application runs on command line. When you run the application, it will prompt you to enter ingredients. Application will search for recipes using these ingredients and will print the result on command prompt. 

Recipe names will be mentioned in Green color, and if there are any ingredients missing from the recipe then they'll appear in red color.


## Setup
* **Get API Key** Before using this application, you must retrieve an API key from Spoonacular. You can create a free account and get an API key by visiting [https://spoonacular.com/food-api](https://spoonacular.com/food-api)
* **Set API Key In Environment** For security purpose, application accesses api key from environment variable with variable name **SPOON_API_KEY**. Open terminal and run below command with your API Key before running python script
```bash
export SPOON_API_KEY=<KEY>
```

* **Import python library 'requests'** Application uses request library to make HTTP calls. Use below command to import the library
```bash
pip3 install requests
```

* **Import python library 'termcolor'** To print results in various colors, application uses termcolor python library. Use below command to import the library
```bash
pip3 install termcolor
```

## Run
Use below steps to run the application 
* Checkout the application from git repository
* Open terminal and goto poroject directory.
* If you didnt set SPOON_API_KEY in bash profile and closed previous terminal session, then you should set API key again before running application
* Run below command to run the application and follow the command prompt
```bash
python run.py
```

## Test
To unit test application, please follow below steps 
* Open terminal and goto poroject directory
* Run below command to unit test the application
```bash
python test.py
```
