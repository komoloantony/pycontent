def contact_book():
    contacts={}
    n = int(input("How many contacts are you putting: "))

    for i in range(n):
        name = input(f"Enter name {i+1}: ").title().strip()
        phone = input("Enter phone number: ")
        if len(phone) == 10 and phone.isdigit():
            contacts[name]= phone
        else:
            print("\n invalid input! ")
            phone = input("Enter phone nuber: ")
            contacts[name]=phone

    print("\n -------PHONE NUMBERS------- ")

    for name in sorted(contacts.keys()) :
        print(f"{name}:[{contacts[name]}]")

contact_book()
