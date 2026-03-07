#where we get the 2D module of the turtles that will be used in the race and time
import turtle
import time
import random

#where we will create the display of the race
WIDTH , HEIGHT = 500,500                        #we display the height and the width of the screen
COLORS = ["red","green","brown","black","yellow","blue","pink"]

#where we create the screen


#where the number of turtles are being generated
def num_of_turtles():
    racers = 0
    
    #where we ensure the user puts the right number of racers as required and its an integer
    while True:     
        racers = input("Enter the number of racers (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("INVALID INPUT,TRY AGAIN!")
            continue
        
        if 2<= racers <=10:     #we check if the number inputed is in range
            return racers
        else:
            print("NUMBER NOT IN RANGE,TRY AGAIN!")

def create_turtles(colors) :
    turtles=[]
    spacingx = WIDTH // (len(colors) + 1)
    for i , color in enumerate(colors):     #we get the index and value of the colors 
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i+1) *spacingx, -HEIGHT//2 + 20)            #set the posistoning of the turtules
        racer.pendown()
        turtles.append(racer) 
   
    return turtles

def race(colors):
    turtles = create_turtles(colors)   
    
    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)         
            
            x,y = racer.pos()
            if y >= HEIGHT // 2-10:
                return colors[turtles.index(racer)] 
            



def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("TURTLE RACE")
   
racers = num_of_turtles()       #where we call out the the function
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]
print(colors)
winner = race(colors)
print("The winner is: ",winner)
time.sleep(5)

