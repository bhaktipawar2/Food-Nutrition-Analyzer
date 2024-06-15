import streamlit as st
import pandas as pd

# Title of the application
st.title('Food Nutrition Analyzer')

# Sidebar for user input
st.sidebar.title('User Input')
food_name = st.sidebar.text_input('Enter food name', 'banana')

# API call to fetch nutrition data (assuming you have an API to fetch data)
# Replace this with your actual API call logic
# Example: Here we're assuming we have a function get_nutrition_data() that fetches data
def get_nutrition_data(food_name):
    # Your API call logic here
    # Example: Using a placeholder function
    # nutrition_data = get_nutrition_data_from_api(food_name)
    nutrition_data = {
        'Food': ['Banana', 'Apple'],
        'Calories': [89, 52],
        'Protein (g)': [1.1, 0.3],
        'Fat (g)': [0.3, 0.2],
        'Carbs (g)': [22.8, 14],
        'Fiber (g)': [2.6, 2.4]
    }
    return pd.DataFrame(nutrition_data)

nutrition_df = get_nutrition_data(food_name)

# Display nutrition data
st.subheader('Nutrition Information for {}'.format(food_name))
st.write(nutrition_df)

# Optionally, you can add more features like charts, additional inputs, etc.