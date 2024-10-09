import requests
from bs4 import BeautifulSoup
import pandas as pd

# Dummy data for simulation
restaurant_data = {
    'McDonald’s': [
        {'item': 'Big Mac', 'calories': 540, 'price': 3.99},
        {'item': 'McChicken', 'calories': 400, 'price': 1.29},
        {'item': 'Large Fries', 'calories': 510, 'price': 2.19}
    ],
    'Burger King': [
        {'item': 'Whopper', 'calories': 657, 'price': 4.19},
        {'item': 'Chicken Fries', 'calories': 280, 'price': 3.49},
        {'item': 'Onion Rings', 'calories': 500, 'price': 2.49}
    ],
    'Wendy’s': [
        {'item': 'Baconator', 'calories': 950, 'price': 5.19},
        {'item': 'Spicy Chicken Sandwich', 'calories': 500, 'price': 4.99},
        {'item': 'Small Fries', 'calories': 320, 'price': 1.79}
    ]
}

def calculate_calories_per_dollar(menu_item):
    return menu_item['calories'] / menu_item['price']

def get_restaurant_data(restaurant_name):
    # Placeholder: Normally, you would scrape the restaurant’s website or use their API.
    # Here we use the simulated data from `restaurant_data` dictionary.
    if restaurant_name in restaurant_data:
        return restaurant_data[restaurant_name]
    else:
        return []

def main():
    # Step 1: Get input from the user
    restaurants = input("Enter a list of fast food restaurants separated by commas: ").split(',')

    # Step 2: Initialize an empty list to store all the items with their calories per dollar
    items_with_cpd = []

    # Step 3: Loop through each restaurant and fetch their data
    for restaurant in restaurants:
        restaurant = restaurant.strip()  # Remove leading/trailing spaces
        print(f"Fetching data for {restaurant}...")

        menu_items = get_restaurant_data(restaurant)
        if menu_items:
            for item in menu_items:
                cpd = calculate_calories_per_dollar(item)
                items_with_cpd.append({
                    'restaurant': restaurant,
                    'item': item['item'],
                    'calories': item['calories'],
                    'price': item['price'],
                    'calories_per_dollar': cpd
                })
        else:
            print(f"No data found for {restaurant}")

    # Step 4: Sort the items by calories per dollar in descending order
    sorted_items = sorted(items_with_cpd, key=lambda x: x['calories_per_dollar'], reverse=True)

    # Step 5: Display the sorted items
    df = pd.DataFrame(sorted_items)
    print("\nItems sorted by Calories per Dollar (Descending):")
    print(df[['restaurant', 'item', 'calories', 'price', 'calories_per_dollar']])

if __name__ == "__main__":
    main()
