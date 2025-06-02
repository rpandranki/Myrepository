meal_cost = float(input("Enter the cost of the meal: $"))

tip = meal_cost * 0.18

tax = meal_cost * 0.07

total = meal_cost + tip + tax

print(f"Tip (18%): ${tip:.2f}")

print(f"Tax (7%): ${tax:.2f}")

print(f"Total Amount: ${total:.2f}")

