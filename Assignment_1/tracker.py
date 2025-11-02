# ============================================================
# Project Title: Daily Calorie Tracker (CLI)
# Author: Ujjawal Tiwari
# Date: November 2025
# Course: Programming for Problem Solving using Python
# ============================================================

import datetime  # for timestamp in bonus task

# -------------------------------
# Task 1: Setup & Introduction
# -------------------------------
print("🍎 Welcome to the Daily Calorie Tracker!")
print("This tool helps you record your daily meals and track your calorie intake.\n")

# -------------------------------
# Task 2: Input & Data Collection
# -------------------------------
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

# -------------------------------
# Task 3: Calorie Calculations
# -------------------------------
total_calories = sum(calorie_values)
average_calories = total_calories / len(calorie_values)

daily_limit = float(input("\nEnter your daily calorie limit: "))

# -------------------------------
# Task 4: Exceed Limit Warning System
# -------------------------------
if total_calories > daily_limit:
    status_message = "⚠️ You have exceeded your daily calorie limit! Try to eat lighter next time."
else:
    status_message = "✅ Great job! You’re within your daily calorie limit."

# -------------------------------
# Task 5: Neatly Formatted Output
# -------------------------------
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


save_option = input("\nWould you like to save this session to a file? (yes/no): ").strip().lower()

if save_option == "yes":
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"calorie_log_{timestamp}.txt"

    with open(filename, "w") as file:
        file.write("Daily Calorie Tracker Log\n")
        file.write(f"Date/Time: {datetime.datetime.now()}\n")
        file.write("---------------------------------------------\n")
        file.write(f"{'Meal Name':<20}{'Calories':>10}\n")
        file.write("---------------------------------------------\n")

        for i in range(num_meals):
            file.write(f"{meal_names[i]:<20}{calorie_values[i]:>10.2f}\n")

        file.write("---------------------------------------------\n")
        file.write(f"{'Total:':<20}{total_calories:>10.2f}\n")
        file.write(f"{'Average:':<20}{average_calories:>10.2f}\n")
        file.write("---------------------------------------------\n")
        file.write(status_message + "\n")

    print(f"\n💾 Session saved successfully as '{filename}'!")
else:
    print("\nSession not saved. Thank you for using the tracker!")

print("\n👋 Goodbye! Stay healthy and mindful of your meals!")
