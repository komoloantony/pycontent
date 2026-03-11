#where we import the necessary modules of the program
import time
import pygame

pygame.init()   #where we initialize the pygame module where we will generate the sound

#where we define the constants of the program
CLEAR = "\033[2J"  
CLEAR_AND_RETURN = "\033[H"

#where we create the alarm function
def alarm(seconds):
    time_elapsed = 0
    
    #where we create the loop that will run the alarm
    while time_elapsed < seconds:
       time_left = seconds - time_elapsed
       minutes_left = time_left // 60
       seconds_left = time_left % 60
             
       print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")
    
       time.sleep(1)
       time_elapsed += 1
   
        
def sound_alarm():
    pygame.mixer.init()
    pygame.mixer.music.load("Undertaker's Bell - Tntdcostanza (youtube).mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

minutes = int(input("How many minutes to wait: "))
total_seconds = minutes * 60

alarm(total_seconds)
sound_alarm()

print("ALARM DONE!")