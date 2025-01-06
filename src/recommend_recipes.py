import pandas as pd
import json

# Function to recommend recipes based on health goals
def recommend_recipes(optimized_recipes_df, user_input):
    # Extract user health goal
    health_goal = user_input.get("health_goals", "").lower()

    # Define macronutrient ratios for different health goals
    goal_macronutrient_ratios = {
        "low-carb": {"protein": 0.4, "total_fat": 0.5, "carbohydrates": 0.1},
        "high-protein": {"protein": 0.6, "total_fat": 0.3, "carbohydrates": 0.1},
        "balanced": {"protein": 0.33, "total_fat": 0.33, "carbohydrates": 0.34}
    }

    # Default to "balanced" if no goal is specified or if it's an unknown goal
    ratios = goal_macronutrient_ratios.get(health_goal, goal_macronutrient_ratios["balanced"])

    # Filter recipes based on the fitness score that aligns with user's health goal
    optimized_recipes_df["fitness_score"] = (
        optimized_recipes_df["protein_percentage"] * ratios["protein"] +
        optimized_recipes_df["total_fat_percentage"] * ratios["total_fat"] +
        optimized_recipes_df["carbohydrates_percentage"] * ratios["carbohydrates"]
    )

    # Sort the recipes by fitness score in descending order
    sorted_recipes = optimized_recipes_df.sort_values(by="fitness_score", ascending=False)

    # Recommend top 3 recipes
    top_3_recipes = sorted_recipes.head(3)

    return top_3_recipes[['name', 'fitness_score', 'calories', 'ingredients']]

# Load the optimized recipes dataset
def load_optimized_recipes(file_path):
    return pd.read_csv(file_path)

# Load user input (health goals)
def load_user_input(file_path):
    with open(file_path, 'r') as f:
        user_input = json.load(f)
    return user_input

if __name__ == "__main__":
    # Define paths
    optimized_recipes_path = "../data/optimized_recipes.csv"
    user_input_path = "../data/user_input.json"

    # Load datasets
    optimized_recipes_df = load_optimized_recipes(optimized_recipes_path)
    user_input = load_user_input(user_input_path)

    # Recommend recipes based on health goal
    recommended_recipes = recommend_recipes(optimized_recipes_df, user_input)

    # Print the top 3 recommended recipes
    print("Top 3 Recommended Recipes based on your health goals:")
    print(recommended_recipes)
