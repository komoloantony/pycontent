import curses               
from curses import wrapper
import queue
import time

maze=[
["#","O","#","#","#","#","#","#","#"],
["#"," "," "," "," "," "," "," ","#"],
["#"," ","#","#"," ","#","#"," ","#"],
["#"," ","#"," "," "," ","#"," ","#"],
["#"," ","#"," ","#"," ","#"," ","#"],
["#"," ","#"," ","#"," ","#"," ","#"],
["#"," ","#"," ","#"," ","#","#","#"],
["#"," "," "," "," "," "," "," ","#"],
["#","#","#","#","#","#","#","X","#"]
]

def print_maze(maze,stdscr,path=[]):
    RED = curses.color_pair(1)
    BLUE = curses.color_pair(2)
    
    for i,row in enumerate(maze):       #we draw the rows
        for j,value in enumerate(row):  #we draw the column
            if(i,j) in path:
              stdscr.addstr(i,j*2,"*",RED)  
            else:
              stdscr.addstr(i,j*2,value,BLUE)    
        

def find_start(maze,start):
    for i,row in enumerate(maze):
        for j,value in enumerate(row):
            if value == start:
                return i,j
    return None     

        
def find_path(maze,stdscr):
    start = "O"
    end = "X"   
    start_pos = find_start(maze,start)
    
    q = queue.Queue()
    q.put((start_pos,[start_pos])) 
    
    visited = set()
    visited.add(start_pos)
    
    while not q.empty():
        current_pos ,path = q.get()
        row , col = current_pos
    
        if maze[row][col] == end:
            return path
                    
        stdscr.clear()  #where we clear the screen
        print_maze(maze,stdscr,path) #where we print the maze
        time.sleep(0.3)
        stdscr.refresh()    #where we refresh the screen
       
        neighbors = find_neighbours(maze,row,col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue
            
            x,y = neighbor
            
            if maze [x][y] == "#":
                continue
            
            new_path = path+[neighbor]
            q.put((neighbor,new_path))
            visited.add(neighbor)
                

def find_neighbours(maze,row,col):
    neighbours = []
    
    if row > 0: #up in the row
        neighbours.append((row -1,col))    
    if row + 1 <len(maze): #down in the row
        neighbours.append((row + 1,col))
        
    if col > 0: #left for the columns
        neighbours.append((row ,col-1))
    if col + 1 < len(maze[0]):  #right for the columns
        neighbours.append((row,col + 1))   
        
    return neighbours          
                   
#where we define the main function 
def main(stdscr): 
    curses.start_color()
    curses.init_pair(1,curses.COLOR_RED , curses.COLOR_BLACK)     #we create a color pair for the red and black color for the path
    curses.init_pair(2,curses.COLOR_BLUE , curses.COLOR_BLACK)    #we create another pair for the obstacles

    find_path(maze,stdscr)
    stdscr.getch()      #where we wait for the user to press a key to clear the screen and continue the program
    
wrapper(main)       #where we call the main function with the wrapper function
print("You have found your destination😁")