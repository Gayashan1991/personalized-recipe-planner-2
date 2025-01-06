# Import libraries
import pandas as pd
import json
import os

# Define paths
data_path = "../data/filtered_recipes.csv"
user_input_path = "../data/user_input.json"

# Load preprocessed dataset
if os.path.exists(data_path):
    recipes_df = pd.read_csv(data_path)
    print("Filtered recipes dataset loaded successfully!")
else:
    raise FileNotFoundError(f"Preprocessed dataset not found at {data_path}. Please run Step 1 first.")

# Load user input
if os.path.exists(user_input_path):
    with open(user_input_path, "r") as file:
        user_input = json.load(file)
    print("User input loaded successfully!")
else:
    raise FileNotFoundError(f"User input file not found at {user_input_path}. Please run Step 2 first.")

# Display sample data
print("Sample Recipes Data:")
print(recipes_df.head())

# Extract user preferences
dietary_restrictions = user_input.get("dietary_restrictions", [])
excluded_ingredients = user_input.get("excluded_ingredients", [])
calorie_budget = user_input.get("calorie_budget_per_meal", None)

# Filter recipes based on dietary restrictions (tags)
if dietary_restrictions:
    print("\nFiltering based on dietary restrictions:", dietary_restrictions)
    recipes_df = recipes_df[recipes_df['tags'].apply(lambda x: any(tag in x for tag in dietary_restrictions))]

# Exclude recipes with certain ingredients
if excluded_ingredients:
    print("\nExcluding recipes with ingredients:", excluded_ingredients)
    recipes_df = recipes_df[~recipes_df['ingredients'].apply(lambda x: any(ing in x for ing in excluded_ingredients))]

# Filter recipes based on calorie budget
if calorie_budget:
    print("\nFiltering recipes based on calorie budget per meal:", calorie_budget)
    # The `nutrition` column contains a string: "[calories, fat, sugar, protein, carbs, sodium]"
    recipes_df['calories'] = recipes_df['nutrition'].apply(lambda x: float(x.strip('[]').split(',')[0]) if pd.notnull(x) else None)
    recipes_df = recipes_df[recipes_df['calories'] <= calorie_budget]

# Save the filtered results
filtered_results_path = "../data/filtered_user_recipes.csv"
recipes_df.to_csv(filtered_results_path, index=False)
print(f"\nFiltered recipes saved at: {filtered_results_path}")

# Display filtered recipes
print("\nFiltered Recipes:")
print(recipes_df.head())
