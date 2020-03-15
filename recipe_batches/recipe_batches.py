#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = 0  
  while True:
    for key in recipe.keys():
      if key in ingredients.keys():
        if ingredients[key]-recipe[key] >= 0:
          new_value = ingredients[key]-recipe[key]
          ingredients.update({key:new_value})
        else:
          return batches
      else:
        return 0
    batches += 1



# if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
ingredients = { 'milk': 132, 'butter': 51, 'flour': 51 }
  # print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
print(recipe_batches(recipe, ingredients))