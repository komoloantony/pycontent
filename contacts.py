def contact_book():
    contacts={}
    n = int(input("How many contacts are you putting: "))

    for i in range(n):
        name = input(f"Enter name {i+1}: ").title().strip()
        phone = int(input("Enter phone number: "))
        contacts[name]=phone

    print("\n -------PHONE NUMBERS------- ")

    for name,phone in contacts.items():
        print(f"{name}:[{phone}]")
contact_book()

