# Personalized Recipe Recommender with Nutritional Optimization

This project is a personalized recipe recommendation system that suggests recipes based on user preferences, health goals, and nutritional optimization. It uses a dataset of recipes and applies various filters to recommend the best recipes that match the user's health goals (e.g., low-carb, high-protein, balanced). It also allows for the optimization of recipes based on nutritional values.

## Project Structure
```
/personalized-recipe-recommender
    /data
        RAW_recipes.csv                  # Original dataset from Kaggle
        filtered_recipes.csv             # Preprocessed dataset
        user_input.json                  # JSON file for storing user preferences
        filtered_user_recipes.csv        # Filtered recipes based on user input
        optimized_recipes.csv            # Recipes optimized for nutrition
    /notebooks
        01_data_exploration.ipynb        # Jupyter Notebook for Step 1
        02_user_input.ipynb              # Jupyter Notebook for Step 2
        03_recipe_filtering.ipynb        # Jupyter Notebook for Step 3
        04_nutritional_optimization.ipynb  # Jupyter Notebook for Step 4
    /src
        preprocess_data.py               # Script for data cleaning and preprocessing
        filter_recipes.py                # Recipe filtering logic
        optimize_recipes.py              # Recipe optimization logic
        recommend_recipes.py             # New script for recommending recipes based on health goal
    requirements.txt                     # Dependencies for the project
    README.md                            # Project description
```


### Files Description

- `/data/RAW_recipes.csv`: The original dataset containing recipe details from Kaggle (https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions).
- `/data/filtered_recipes.csv`: Preprocessed recipe data after cleaning.
- `/data/user_input.json`: Stores the user's preferences such as health goals and calorie budget.
- `/data/filtered_user_recipes.csv`: Recipes filtered based on user input.
- `/data/optimized_recipes.csv`: Recipes optimized based on the nutritional goals.
- `/notebooks/01_data_exploration.ipynb`: Jupyter notebook for exploring and understanding the dataset.
- `/notebooks/02_user_input.ipynb`: Jupyter notebook for collecting user preferences such as health goals and calorie budget.
- `/notebooks/03_recipe_filtering.ipynb`: Jupyter notebook for filtering recipes based on user input (e.g., vegetarian, vegan).
- `/notebooks/04_nutritional_optimization.ipynb`: Jupyter notebook for optimizing recipes based on nutritional goals (e.g., low-carb, high-protein, balanced).
- `/src/`: Contains Python scripts for preprocessing, filtering, optimizing, and recommending recipes.
    - `preprocess_data.py`: Script to clean and preprocess the recipe data.
    - `filter_recipes.py`: Logic for filtering recipes based on user input.
    - `optimize_recipes.py`: Optimizes recipes based on health goals.
    - `recommend_recipes.py`: Recommends personalized recipes based on optimized recipes and user preferences.
- `requirements.txt`: A file containing all dependencies needed for the project.
- `README.md`: Project description and instructions on how to use the application.

## Installation and Setup

### Prerequisites

Ensure that you have the following software installed:

- Python 3.x
- Jupyter Notebooks (for `.ipynb` notebooks)
- Pandas, NumPy, and other dependencies listed in `requirements.txt`

To install the required Python dependencies, run the following command:

```bash
pip install -r requirements.txt
```

### Running the Project

1. **Step 1**: Data Exploration  
   Open `01_data_exploration.ipynb` in Jupyter Notebook to explore the `RAW_recipes.csv` dataset. This step involves understanding the dataset structure and cleaning it if necessary.

2. **Step 2**: User Input Collection  
   Open `02_user_input.ipynb` in Jupyter Notebook to collect user preferences. The notebook collects information such as health goals (e.g., low-carb, high-protein, balanced) and calorie budget. Save the preferences in the `user_input.json` file.

3. **Step 3**: Recipe Filtering  
   Open `03_recipe_filtering.ipynb` to filter recipes based on user preferences (e.g., vegetarian, vegan, specific ingredients). The filtered data is saved as `filtered_user_recipes.csv`.

4. **Step 4**: Nutritional Optimization  
   Open `04_nutritional_optimization.ipynb` to optimize recipes based on the user's health goals (low-carb, high-protein, balanced). The output of this step is stored in `optimized_recipes.csv`, containing the most nutrition-optimized recipes.

5. **Step 5**: Recipe Recommendation  
   After generating the optimized recipes and user input files, run the Python script `recommend_recipes.py` to get the top 3 recommended recipes based on the user's health goals.

   To run the recipe recommendation script, use the following command:

   ```bash
   python src/recommend_recipes.py
   ```

   This script reads the `user_input.json` and `optimized_recipes.csv` files and prints the top 3 recommended recipes according to the health goal specified by the user.

### Example of Running the Recommendation

Here’s a basic usage example for recommending recipes:

```bash
$ python src/recommend_recipes.py
Top 3 Recommended Recipes based on your health goals:
                         name  fitness_score  calories  ingredients
0         Recipe Name 1          0.85      200     ['ingredient1', 'ingredient2']
1         Recipe Name 2          0.80      250     ['ingredient3', 'ingredient4']
2         Recipe Name 3          0.75      180     ['ingredient5', 'ingredient6']
```

### File Description for Recipe Recommendations

- **user_input.json**: This file stores the user's health goals (e.g., low-carb, high-protein) and calorie budget.
- **optimized_recipes.csv**: Contains recipes that have been optimized for nutritional value according to the user's health goals.

The `recommend_recipes.py` script uses these files to generate personalized recipe recommendations.

## Future Improvements

- **Collaborative Filtering**: Implement collaborative filtering to recommend recipes based on user preferences and reviews.
- **User Feedback**: Add a user feedback mechanism to improve recommendations over time.
- **Advanced Algorithms**: Implement more advanced machine learning algorithms, such as regression models or neural networks, to predict the best recipes for users based on their preferences.

## License

This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for more details.
