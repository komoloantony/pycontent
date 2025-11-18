import tkinter as tk

contacts = {}

def add_contact():
    name = name_entry.get().title().strip()
    phone = phone_entry.get().strip()

    if len(phone) == 10 and phone.isdigit():
        contacts[name] = phone
        result_label.config(text=f"Saved: {name} - {phone}")
    else:
        result_label.config(text="Invalid phone number!")

def show_contacts():
    output = ""
    for name in sorted(contacts.keys()):
        output += f"{name}: {contacts[name]}\n"
    result_label.config(text=output)

window = tk.Tk()
window.title("CONTACT BOOK")

tk.Label(window, text="Name:").pack()
name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window, text="Phone:").pack()
phone_entry = tk.Entry(window)
phone_entry.pack()

add_button = tk.Button(window, text="Add Contact", command=add_contact)
add_button.pack()

show_button = tk.Button(window, text="Show Contacts", command=show_contacts)
show_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()

