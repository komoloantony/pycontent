master_password = input("What is your password? ")  #ask the user what is their password

def view():
    with open("Password.txt", "r") as f:  # we create a file where the passwords will be viewed
        for line in f:
            data = line.rstrip()
            name,pwd = data.split("|")
            print("USER:",name,"PASSWORD:",pwd)
            print("------------------------- \n")



def add():  #this is the add function where the new password will be stored in a text file
    name = input("Account name: ")
    password = input("Password: ")

    with open("Password.txt", "a") as f:      #we create a file where the passwords will be stored
        f.write(name +  "|"  + password + "\n" )

#main program
while True:
   mode = input("Would you lime to add a new password or view existing ones(view , add)?. You can also press q to quit: ").lower()     #here we ask the user if they want to add a new password or just view the exsiting ones stored before

   if mode == "q":      #here the program will end if the user presses "q" to quit
      break
   elif mode == "view":   #if the user says view it will call view function
       view()
   elif mode == "add":    # it will call add function
       add()
   else:
       print("INVALID MODE!")       #if the user puts anything else
       continue
