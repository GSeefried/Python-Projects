print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? "))

tip = int(input("What percentage would you like to tip? 10, 12, or 15? "))

split = int(input("How many people are splitting the bill? "))

total = float((bill / split) * ((100 + tip) / 100))

print(f"Each person should pay ${total:.2f}")