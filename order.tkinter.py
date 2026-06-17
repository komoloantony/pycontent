import tkinter as tk
from tkinter import simpledialog, messagebox


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

total_cost = 0
order_summary = []

def greet_customer():
    global customer_name
    customer_name = simpledialog.askstring("Welcome", "Please enter your name:").title().strip()
    mood = simpledialog.askstring("Mood", f"Hello {customer_name}. How are you doing today?").lower().strip()

    bad_moods = ["bad", "sad", "tired", "not good", "terrible", "awful"]
    good_moods = ["good", "fine", "amazing", "great", "awesome"]

    if mood in bad_moods:
        messagebox.showinfo("Mood", "I’m sorry 😔. All shall be well, just stay strong.")
    elif mood in good_moods:
        messagebox.showinfo("Mood", f"That's great to hear, {customer_name}! 😊")
    else:
        messagebox.showinfo("Mood", "Thank you for sharing. I hope your day goes well!")

def place_order():
    global total_cost, order_summary
    item = item_entry.get().lower().strip()
    
    if item == "done":
        messagebox.showinfo("Total", f"Your total bill is: sh.{total_cost}\nThank you for ordering with us! 😊")
        root.destroy()
        return
    
    if item not in menu:
        messagebox.showerror("Error", "❌ Item not in the menu. Try again.")
        return
    
    try:
        quantity = int(quantity_entry.get())
    except:
        messagebox.showerror("Error", "❌ Invalid number. Try again.")
        return
    
    cost = menu[item] * quantity
    total_cost += cost
    order_summary.append(f"{quantity} x {item} → sh.{cost}")
    
    order_text.set("\n".join(order_summary))
    item_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Food Ordering System")
root.geometry("400x500")

root.after(100, greet_customer)


menu_text = "MENU:\n" + "\n".join([f"{item.title()} - sh.{price}" for item, price in menu.items()])
menu_label = tk.Label(root, text=menu_text, justify="left")
menu_label.pack(pady=10)

item_entry = tk.Entry(root)
item_entry.pack(pady=5)
item_entry.insert(0, "Enter item name")

quantity_entry = tk.Entry(root)
quantity_entry.pack(pady=5)
quantity_entry.insert(0, "Enter quantity")

order_btn = tk.Button(root, text="Add to Order", command=place_order)
order_btn.pack(pady=10)


order_text = tk.StringVar()
order_label = tk.Label(root, textvariable=order_text, justify="left")
order_label.pack(pady=10)

root.mainloop()
