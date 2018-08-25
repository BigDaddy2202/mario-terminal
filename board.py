import colors as cl
from os import system
class Board:
# ------------------------------------------------------------------------------------
    '''initialising board'''
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.board = [[ [] for j in range(self.width)] for i in range(0, self.height)]
        self.render()
# ------------------------------------------------------------------------------------
    def render(self):

        non_floor = []
        floor = [ (cl.colors['Brown']+' '+cl.colors['brk']) for i in range(0, self.width)]

        for i in range(0, self.width):

            non_floor.append(cl.colors['back']+' '+cl.colors['brk'])

        for i in range(0, self.height):

            if i < (self.height*(4/5)) :
                self.board[i] = non_floor[:]

            else :
                self.board[i] = floor[:]

        self.printb(0)
# ------------------------------------------------------------------------------------
    '''function to keep updating the board in main loop'''

    def printb(self,w):

        temp = ['' for i in range(0, self.height)]

        for j in range(0, self.height):
            for i in range(0, 140):
                temp[j] = temp[j] + self.board[j][i+w]

        system('clear')
        for i in range(0, self.height):
            print(temp[i])
# ------------------------------------------------------------------------------------
    '''function to detect different types of collisions'''
    def detectcollision(self,x , y):

        if self.board[y-1][x] == '/' or self.board[y-1][x] == '\\':
            return 'mario_stan'

        elif self.board[y][x-1] == cl.colors['Purple']+'/'+cl.colors['brk'] or self.board[y][x-1] == cl.colors['Purple']+'\\'+cl.colors['brk']:
            return 'mario'

        elif self.board[y][x-1] == cl.colors['Purple']+'*'+cl.colors['brk'] or self.board[y][x-1] == cl.colors['Purple']+'*'+cl.colors['brk']:
            return 'mario'

        elif self.board[y][x+2] == cl.colors['back']+' '+cl.colors['brk'] and self.board[y-1][x+2]== cl.colors['back']+' '+cl.colors['brk']:
            return 'empty'


        elif self.board[y-1][x] == '/' or self.board[y-1][x]== '\\':
            return 'enemy'

        elif self.board[y][x+1] == 'S':
            return 'senemy'


        elif self.board[y+1][x] == 'U' or self.board[y+1][x+1] == 'U' or self.board[y][x] == 'U':
            return 'hackerman'

        elif self.board[y][x+3] == '1' or self.board[y][x+3] == '0':
            return 'brick'

        elif self.board[y-1][x] == '1' or self.board[y-1][x] == '0':
            return 'brick'

        elif self.board[y+1][x] == '1' or self.board[y+1][x] == '0':
            return 'stan_brick'

# ------------------------------------------------------------------------------------
    '''specifaclly to detect coin using co-ordinates'''
    def detectcoin(self, x, y, mario):
        if (x==mario.x+1 or x==mario.x) and (y == mario.y-3):
            return 1
        if (x+1==mario.x+1 or x+1==mario.x) and (y == mario.y-3):
            return 1
        if (x+2==mario.x+1 or x+2==mario.x) and (y == mario.y-3):
            return 1
        else: return 0
# ------------------------------------------------------------------------------------
    '''detect standing mario'''
    def detectstan(self,x ,y, mario):
        if x== mario.x and y == mario.y +1:
            return 'stand'
        elif x == mario.x+1 and y == mario.y +1:
            return 'stand'

        else: return 'not'
# ------------------------------------------------------------------------------------
    '''All functions below uses co-ordinated to find out different collisions maybe below or at side etc'''
    def emptybelow(self,x,y):
        if self.board[y+1][x] == cl.colors['back']+' '+cl.colors['brk'] and self.board[y+1][x+1] == cl.colors['back']+' '+cl.colors['brk']:
            return 'empty'

        else :
            return 'not empty'
# ------------------------------------------------------------------------------------
    def detectside(self,x,y,brick):
        if (x == brick.x or x+1==brick.x)and (y == brick.y or y-1 == brick.y):
            return 'side'
        if (x == brick.x + 2 or x+1==brick.x + 2)and (y == brick.y or y-1 == brick.y):
            return 'side'
        else:
            return 'else'
# ------------------------------------------------------------------------------------
    def detectbrick(self,x,y,mario):
        if (x == mario.x or x== mario.x+1) and y == mario.y -3:
            return 'mario'
        else: return 'no'
# ------------------------------------------------------------------------------------
    def destroy(self,x,y,mario):
        if (x == mario.x or x ==mario.x+1) and (y == mario.y +2):
            return 'kill'

        elif (x+1 == mario.x or x+1 ==mario.x+1) and (y == mario.y +2):
            return 'kill'
        else:
            return 'gandhiji'
# ------------------------------------------------------------------------------------
    def detpip(self,x,y,p):
        if(x==p.x-1) and (y==p.y or y==p.y-1 or y==p.y-2 or y==p.y-3 or y==p.y-4 or y==p.y-5 ):
            return 'stop'
        if (x==p.x or x==p.x+1 or x==p.x+2 )  and (y==p.y-1):
            return 'proceed'
        if (x+1==p.x or x+1==p.x+1 or x+1==p.x+2 )  and (y==p.y-1):
            return 'proceed'
# ------------------------------------------------------------------------------------
    def detectmar(self,x,y,mario):
        if (x==mario.x +2 or x==mario.x+3 ) and y == mario.y :
            return True
        if (x==mario.x +2 or x==mario.x+3 ) and y == mario.y+1 :
            return True
        else:
            return False
# ------------------------------------------------------------------------------------
    def detect_touch(self,x,y,mario):
        if (mario.x==x) and (y == mario.y-3 or y==mario.y +1):
            return True
        elif x==mario.x+1 and y==(mario.y-2 or mario.y-1 or mario.y):
            return True
        elif x+1==mario.x and y==(mario.y-2 or mario.y-1 or mario.y):
            return True
        else:
            return False
# ------------------------------------------------------------------------------------
    def det(self,x,y,mario):
        if x-2== (mario.x+1 or mario.x +2 or mario.x +3) and y== (mario.y or mario.y-1 or mario.y -2):
            return True

        if x-1== (mario.x+1 or mario.x +2 or mario.x +3) and y== (mario.y or mario.y-1 or mario.y -2):
            return True
        if x+1== (mario.x+1 or mario.x +2 or mario.x +3) and y== (mario.y or mario.y-1 or mario.y -2):
            return True
        if x+2== (mario.x+1 or mario.x +2 or mario.x +3) and y== (mario.y or mario.y-1 or mario.y -2):
            return True
        if x+3== (mario.x+1 or mario.x +2 or mario.x +3) and y== (mario.y or mario.y-1 or mario.y -2):
            return True
        else:
            return False

# ------------------------------------------------------------------------------------
    def stop(self,x,y,object):
        if (y or y-1 or y-2)==object.y and x+1 ==(object.x-1 or object.x-2 or object.x-3):
            return True

        if (y or y-1 or y-2)==object.y and x+1 ==(object.x+2 or object.x+1 or object.x):
            return True

        if (y or y-1 or y-2)==object.y and x ==(object.x+2 or object.x+1 or object.x):
            return True

        else:
            return False
# ------------------------------------------------------------------------------------
    def die(self, x, y):
        if (y<=30 and y >20) and (x>=390 and x<416):
            return True
        else:
            return False
# ------------------------------------------------------------------------------------
    def fall(self,x,y,pit):

        if (x >= pit and x <= pit +15) and y == 30:
            return True
        else:
            return False
# ------------------------------------------------------------------------------------
