print("WELCOME TO THE BIBLE QUIZ😁")  #welcome the user to my quiz

playing=input("Do you want to answer the Quiz? ") #ask the user to play the game

#Want to know if the user wants to answer or not
if playing.upper().strip() != "YES":
    quit()

print("Great welcome to the Bible quiz😁")

#to track the score of the user after answering the quiz
total = 0

#the section of the quiz
#the if statment is to check if the answers are correct or not
answer=input("1. Who built the Ark in the Bible? ").strip().title()
if answer == "Noah":
    print("Correct ✔")
    total += 2
else:
    print("Incorrect ❌")

answer=input("2.Who was the wisest man in the Bible? ").strip().title()
if answer == "Solomon":
    print("Correct ✔")
    total += 2
else:
    print("Incorrect ❌")

answer=input("3. Who was known as the father of faith? ").strip().title()
if answer == "Abraham":
    print("Correct ✔")
    total += 2
else:
    print("Incorrect ❌")

answer=input("4. Who was the first King of Israel? ").strip().title()
if answer == "Saul":
    print("Correct ✔")
    total += 2
else:
    print("Incorrect ❌")

answer=input("5. Which prophet was known as the The Prophet Of Doom? ").strip().title()
if answer == "Jeremiah":
    print("Correct ✔")
    total += 2
else:
    print("Incorrect ❌")

answer=input("6.How many people did Jesus feed in with Two FISH and Five LOAVES OF BREAD ? ").strip().title()
if answer == "5000":
    print("Correct ✔")
    total += 2
else:
    print("Incorrect ❌")

answer=input("7. Who denied Jesus? ").strip().title()
if answer == "Judas":
    print("Correct ✔")
    total += 2
else:
    print("Incorrect ❌")

answer=input("8.Who interpreted dreams in the bible ? ").strip().title()
if answer == "Joseph":
    print("Correct ✔")
    total += 2
else:
    print("Incorrect ❌")

answer=input("9. How many disciples did Jesus have? ").strip().title()
if answer == "12":
    print("Correct ✔")
    total += 2
else:
    print("Incorrect ❌")

answer=input("10.Who was the mother of prophet Samuel? ").strip().title()
if answer == "Hannah":
    print("Correct ✔")
    total += 2
else:
    print("Incorrect ❌")

#the user is told the total score of the quiz
print("You got "  +  str(total)  +  " questions correct")
print("You got "  +  str((total / 10) * 100)  +  "%")