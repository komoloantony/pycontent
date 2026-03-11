import random
import string

def generate_password(min_length,number=True,special_characters=True): #we difine a function where it ha sarrguments that ask the user to define the length of the password numbers or special character
    #we are going to generate variables that give us all alpahbets punctuation and numbers
    letters = string.ascii_letters
    numbers = string.digits
    special = string.punctuation
     
    #
    character = letters
    if number:
        character += numbers
    if special_characters:    
        character += special
    
    
    pwd = ""
    meet_criteria = False
    has_number = False
    has_special = False 
    
    while not meet_criteria or len(pwd) < min_length:   #we create a loop that sees if yhe password entered meets the criteria needed 
        new_char = random.choice(character)
        pwd += new_char
        
        if new_char in numbers:
            has_number = True
        elif new_char in special:
            has_special = True
        
        meet_criteria = True
        if number:
            meet_criteria = has_number
        if special_characters:
            meet_criteria = meet_criteria and has_special
            
    return pwd  

min_length =int(input("Enter the minimum length: "))      
has_number = input("Do you want numbers(Y/N): ").lower() == "y" 
has_special = input("Do you want to have special characters(Y/N): ").lower() =="y"
pwd = generate_password(min_length ,has_number,has_special)    
   

print("The generated password is:",pwd)
   