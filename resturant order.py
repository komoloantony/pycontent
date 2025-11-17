def greet_customer():
    name = input("Please enter your name: ").title().strip()
    mood = input(f"Hello {name}. How are you doing today? ").lower().strip()

    bad_moods = ["bad", "sad", "tired", "not good", "terrible", "awful"]
    good_moods = ["good", "fine", "amazing", "great", "awesome"]

    if mood in bad_moods:
        print("I’m sorry 😔. All shall be well, just stay strong.")
    elif mood in good_moods:
        print(f"That's great to hear, {name}! 😊")
    else:
        print("Thank you for sharing. I hope your day goes well!")

    return name


greet_customer()

menu = {
    "chips": 150,
    "burger": 300,
    "soda": 70,
    "pizza": 850,
    "hotdog": 200,
    "shawarma": 350,
    "fries": 120,
    "chicken": 500,
    "coffee": 100,
    "tea": 50,
    "water": 40,
    "icecream": 150,
    "milkshake": 250,
    "sandwich": 180,
    "omelette": 120
}

print("\n--- MENU ---")
for item, price in menu.items():
    print(f"{item.title()} - sh.{price}")

print("\nType 'done' to finish your order.\n")

total_cost = 0

while True:
    item = input("Please place your order: ").lower().strip()

    if item == "done":
        break

    if item not in menu:
        print("❌ Item not in the menu. Try again.")
        continue

    try:
        quantity = int(input("How many: "))
    except:
        print("❌ Invalid number. Try again.")
        continue

    cost = menu[item] * quantity
    total_cost += cost

    print(f"Added {quantity} x {item} → sh.{cost}\n")

print(f"\nYour total bill is: sh.{total_cost}")
print("Thank you for ordering with us! 😊")
