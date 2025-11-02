
# Project Title: Daily Calorie Tracker
# Author: Ujjawal Tiwari
# Date: November 2025
# Course: Programming for Problem Solving using Python

print("🍎 Welcome to the Daily Calorie Tracker!")
print("This tool helps you record your daily meals and track your calorie intake.\n")

meal_names = []
calorie_values = []

num_meals = int(input("How many meals do you want to enter today? "))

for i in range(num_meals):
    print(f"\nMeal {i + 1}:")
    meal = input("Enter meal name: ")
    calories = float(input("Enter calories for this meal: "))
    meal_names.append(meal)
    calorie_values.append(calories)

print("\n✅ Meal data recorded successfully!")

total_calories = sum(calorie_values)
average_calories = total_calories / len(calorie_values)

daily_limit = float(input("\nEnter your daily calorie limit: "))

if total_calories > daily_limit:
    status_message = "⚠️ You have exceeded your daily calorie limit! Try to eat lighter next time."
else:
    status_message = "✅ Great job! You’re within your daily calorie limit."

print("\n📋 Daily Calorie Summary")
print("---------------------------------------------")
print(f"{'Meal Name':<20}{'Calories':>10}")
print("---------------------------------------------")

for i in range(num_meals):
    print(f"{meal_names[i]:<20}{calorie_values[i]:>10.2f}")

print("---------------------------------------------")
print(f"{'Total:':<20}{total_calories:>10.2f}")
print(f"{'Average:':<20}{average_calories:>10.2f}")
print("---------------------------------------------")
print(status_message)

print("Looking forward to your healthy eating tomorrow! 🍽️ \n")