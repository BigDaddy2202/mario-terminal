------------------------Assignment Mario game-----------------------------
coded by -- Pragun Saxena
roll no. - 20171127

This **README** file contains :
 1. Information About the Game
 2. Rules of the Game
 3. controls
 4. Instructions on how to Run the Code
 5. Requirements

### characters/objects
---------------------

()
**  --- this is mario
/\

1 1 --- this is brick1 with pointed spikes on lower part.if mario collides with spikes then he dies
< >

0 0 --- this is brick0 with pointed spikes on lower part.if mario collides with spikes then he dies
< >

clouds are just white backgrounds(because badal important hai babu)

E E ----- this is normal enemy and your one life will reduce when mario collides with it
U U       on level >=3 this becomes smart enemy because it can follow mario by changing its direction
          mario can kill this enemy by jumping on it and he will get score for this

* * --- this is special  smart enemy whose speed increases with time. it gets activated only when mario
* *     comes at a certain range. and game will get over if mario collides with it

X X --- this is poisonous brick and mario will die if he touches any one of them
X X

______
 \  /
 /  \    ---- this is spring. it works as a normal spring i.e. makes u jump higher
/_|_|_\

 * *
*   * --- this is coin. points are there for collecting it
 * *

    _          _@)@) \  
  _/o\_ _ _ _/~`.`...'~\
 / `,'.~,~.~  .   , . ,
  ( ' _' _ '_` _  '  .    -------- this is boss at final level = 4
 ~V~ V~ V~ V~ ~\ `   ' .
  _/\ /\ /\ /\_/, . ' ,
 < ~ ~ '~`'~'`, .,  .   
  \ ' `_  '`_    _    ',


  pitfalls--- empty spaces where if mario falls then game will end

  pipe at end of every level. jump over the pipe to move to the next level

### About The Game
--------------
this game is clone of mario game built for Assignment 1 of ssas course with the main objective
of the protagonist player to overcome all the obstacles and hurdles that come in between and
reach to the end final boss through series of 4 levels

### Rules
-----

- Mario game can be controlled using 'w', 's' and 'a'
- you have total of 5 lives in the Game
- you are scored on the basis of number of coins collected and number of bricks destroyed and the time you took
  to complete the Game
- you have 500 seconds to complete the game then you will be getting negative score  
- falling into pit will result in game end

###Controls
----------

- standard 'w','a' and 'd'
- press q to quit the game

### running the program
----------------------
- simply do python3 main.py
- no extra modules are required

### directory structue
--------------------
'''
20171127_Assign1
	├── alarmexception.py
	├── board.py
	├── colors.py
	├── gameplay.py
	├── getch.py
	├── main.py
	├── objects.py
	├── README.md
	└── requirements.txt

0 directories, 9 files
'''

### scoring parameter:
- brick0 = 100 points
- brick1 = 50 points
- enemy = 20 points
- boss = 500 points
- coin = 30 points
