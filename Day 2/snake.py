# import curses module
import curses

# import the randint function from the random module
from random import randint

# setup window
curses.initscr()                    # initialize screen
win = curses.newwin(20, 60, 0, 0)   # initialize new window
win.keypad(1)                       # switch primary input method to keypad
curses.noecho()                     # do not repeat each input
curses.curs_set(0)                  # do not show cursor
win.border(0)                       # don't show default border
win.nodelay(1) # -1                 # there should be no delay    

# snake and food
snake = [(4, 10), (4, 9), (4, 8)]   # snake's starting coordinates
food = (10, 20)                     # food's starting coordinates

win.addch(food[0], food[1], '#')    # add character to depict the food

# maing game logic
score = 0                           # initialize score to 0
    
ESC = 27                            # ESC key has ASCII value of 27
key = curses.KEY_RIGHT              # store ASCII value of right key
win.addch(food[0], food[1], 'O')    
while key != ESC:                   # run the game until ESC is pressed
    win.addstr(0, 2, 'Score ' + str(score) + ' ')
    win.timeout(100)                # game runs on 100 milliseconds per frame

    prev_key = key                  
    event = win.getch()
    key = event if event != -1 else prev_key    # handle key input

    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
        key = prev_key                          # for every key that we want to read

    # calculate the next coordinates
    y = snake[0][0]
    x = snake[0][1]
    if key == curses.KEY_DOWN:
        y += 1
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_LEFT:
        x -= 1
    if key == curses.KEY_RIGHT:
        x += 1

    snake.insert(0, (y, x))                     # add new body part for snake when it eats the food

    # check if we hit the border
    if y == 0: break
    if y == 19: break
    if x == 0: break
    if x == 59: break

    # if snake runs over itself
    if snake[0] in snake[1:]: break

    # if snake runs over the food
    if snake[0] == food:
        # eat the food
        score += 1
        food = ()
        if food == ():
            food = (randint(1,18), randint(1,58))
            if food in snake:
                food = ()
        win.addch(food[0], food[1], '#')
    else:
        # move snake
        last = snake.pop()
        win.addch(last[0], last[1], ' ')
    
    win.addch(snake[0][0], snake[0][1], '*')

# end curses window on end of game loop
curses.endwin()
print(f"Final score = {score}")     # print final score

# file handling with txt
outfile = open("Scores.txt",'w')    # open Scores.txt
outfile.write(str(score))           # store the final score in Scores.txt
outfile.close() 
