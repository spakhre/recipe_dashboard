import requests
import sqlite3 as sql
import json
import urllib
from random import randint

FILENAME = "nutrition01.db"
con = sql.connect(FILENAME)
C = con.cursor()

# ID set is used to ensure all recipes have unique ID
IDS = {-1}
Nutrition_APP_ID='94cea5f5',
Nutrition_API_KEY='3c1e612154ff5791acb596441fcbbf7a'

URL = f'https://api.edamam.com/search?/app_id=${Nutrition_APP_ID}&app_key=${Nutrition_API_KEY}'

response = requests.get(URL)
print(response)


# Find Food Nutrition

def display_recipe_labels(data, index):
    """
    Displays all recipe labels from a result of request.
    Returns the max index of list of recipes.
    """
    print()
    for recipe in data:
        index += 1
        print(f"   {index})", recipe['recipe']['label'])
    print()
    return index
