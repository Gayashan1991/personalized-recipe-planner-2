import pandas as pd

def optimize_recipes(recipes_df, user_input):
    if 'nutrition' not in recipes_df.columns:
        raise ValueError("The 'nutrition' column is missing from the recipes data.")

    # Extract user preferences
    health_goal = user_input.get("health_goals", "").lower()
    calorie_budget = user_input.get("calorie_budget_per_meal", None)

    # Macronutrient weightings for different health goals
    goal_macronutrient_ratios = {
        "low-carb": {"protein": 0.4, "total_fat": 0.5, "carbohydrates": 0.1},
        "high-protein": {"protein": 0.6, "total_fat": 0.3, "carbohydrates": 0.1},
        "balanced": {"protein": 0.33, "total_fat": 0.33, "carbohydrates": 0.34}
    }

    # Default to "balanced" if no goal is specified
    ratios = goal_macronutrient_ratios.get(health_goal, goal_macronutrient_ratios["balanced"])

    # Extract macronutrients from the "nutrition" column
    def parse_nutrition(nutrition_str):
        # Check if nutrition_str is null or empty
        if pd.isnull(nutrition_str) or nutrition_str.strip() == "":
            return [None] * 7  # Return 7 None values if the nutrition is missing
    
        # Otherwise, parse the nutrition string and return the appropriate 7 values
        try:
            values = [float(x) for x in nutrition_str.strip("[]").split(",")]
            
            # Ensure it always returns 7 values by padding or truncating the list
            values = values + [None] * (7 - len(values))  # Add None if there are less than 7 values
            return values[:7]  # Return the first 7 values in case there are more
        except ValueError:
            # If the string cannot be parsed, return None for all columns
            return [None] * 7

    # Apply the function and split the "nutrition" column into separate columns
 
    nutrition_data = recipes_df["nutrition"].apply(parse_nutrition)

    # Ensure the data is in the right shape (6 columns)
    if len(nutrition_data) == len(recipes_df):
        # Assign the parsed nutrition data to the appropriate columns in the DataFrame
        nutrition_df = pd.DataFrame(nutrition_data.tolist(), columns=["nutrition_calories", "total_fat", "sugar", "sodium", "protein", "saturated_fat", "carbohydrates"])
        recipes_df = pd.concat([recipes_df, nutrition_df], axis=1)
    else:
        raise ValueError("Mismatch in the length of nutrition data and recipe data.")

    # Normalize macronutrients to percentages
    recipes_df["total_macros"] = recipes_df[["total_fat", "protein", "carbohydrates"]].sum(axis=1)
    for macro in ["total_fat", "protein", "carbohydrates"]:
        recipes_df[f"{macro}_percentage"] = recipes_df[macro] / recipes_df["total_macros"]

    # Calculate a fitness score based on user's health goal
    recipes_df["fitness_score"] = (
        recipes_df["protein_percentage"] * ratios["protein"] +
        recipes_df["total_fat_percentage"] * ratios["total_fat"] +
        recipes_df["carbohydrates_percentage"] * ratios["carbohydrates"]
    )

    # Filter recipes based on calorie budget
    if calorie_budget:
        recipes_df = recipes_df[recipes_df["calories"] <= calorie_budget]

    # Sort recipes by fitness score in descending order
    optimized_recipes = recipes_df.sort_values(by="fitness_score", ascending=False)

    return optimized_recipes