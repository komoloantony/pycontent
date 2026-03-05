#where we import random numbers and time
import random
import time

operations = ["+","-","/","*"]      #where we define the operations that will be used in this quiz
min_operand = 3                     #where we define the min number used in this quiz
max_operand = 12                    #where we definr the max number in this quiz
total_problems = 10


#where we definr the function to generate the problems
def generate_problem():         
    left = random.randint(min_operand,max_operand)      #the random numbers are generated here both right and left
    right = random.randint(min_operand,max_operand)
    operator = random.choice(operations)        #where we choose the random operator
   
    exp = str(left) + " " + operator + " " + str(right)         #how the expression will be diplayed 
    answer = eval(exp)     #where the answer will be evaluated
    
    return exp,answer 

wrong = 0       #where the numberof wrongs will be counted
input("PRESS ENTER TO START😁")
print("-----------------------------")
start_time = time.time()    #where we start the timer

#where we will ask the usr to solve the problems
for i in range(total_problems):     #where we will loop through the total number of problems
    exp , answer = generate_problem()
    while True:
        guess = input("PROBLEM# " + str(i + 1) + ": " + exp + " = ")   #where the user will be ask to solve the problem
        if guess == str(answer):    #if the user gets the answer correct they will be told correct and the loop will break
            print("CORRECT!")
            break
        else:
            print("INCORECTT!")
            wrong += 1      #there will be a wrong added to the wrong variable
    print(exp,answer)
    
print("NICE WORK!") 
print("-------------------------------")   
end_time = time.time()        #where we end the timer
total_time =end_time - start_time       #where we caculate the total time taken to solve the problems