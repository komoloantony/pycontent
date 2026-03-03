import random   #help us import random numbers

def roll():         # the first function where the dice will be rolled
    min_value = 1
    max_vaue = 6
    roll = random.randint(min_value,max_vaue)

    return roll

while True:
    players = input("Enter number of players(1-3): ")       #ask the user to enter the number of players
    if players.isdigit():   #makes sure the input is a number
        players = int(players)
        if 1<= players <= 3:    #if the user enters players the correct number of players the program ends
             break
        else:
            print("Players should be between 1-3 players!")     #if the player enters the wrong number of players the program tells it to put the correct number of plaers
            continue
    else:
        print("INVALID INPUT")
        

#we want to find the scores of the players
max_score = 50
player_score = [0 for _ in  range(players)]

print (player_score)


# Going through our players scores
while max(player_score) < max_score:

   for player_index in range(players):     #to makes sure that every player has their turn to play
       print(f"Player:{player_index + 1} turn has just started!")
       print(f"Your score is {player_score[player_index]}\n")
       current_score = 0

       while True:
            should_roll = input("Would you like to roll (y): ").lower()         #the player is asked if they want to roll and to accept they press y
            if should_roll != "y":
                break

            value = roll()      #where the roll function is called in a value variable
            if value == 1:
                print("You rolled a 1! Turn Done!")     #if the player rolled a 1 it means that they have no points and the turn ends there
                current_score = 0
                break

            else:                                       #if they roll any other number they get a point added according to the number they rolled to
                current_score += value
                print(f"You rolled a : {value} ")

            print(f"Your score is: {current_score}")     #the players score is printed

       player_score[player_index] += current_score
       print(f"Your score is {player_score[player_index]}")
       

#we are able to tell who won
max_score = max(player_score)       #it will go through the scores of the players and tell us who has the highest score
winner = player_score.index(max_score)   #this is where the code tells us where the maximum score is...if its in player 1,2 or 3
print(f"PlAYER {winner + 1} IS THE WINNER WITH A SCORE OF {max_score}!")