import sys
import signal
from random import randint
from board import Board
from alarmexception import AlarmException
from getch import _getChUnix as getChar
from gameplay import Gameplay
import colors as cl
game = Gameplay()
# f=open('debug.txt', 'w')
sp = cl.colors['back']+' '+cl.colors['brk']

'''if string generate comes in any function then it means function to spawn on board'''

'''if shape or update string comes in any function then it means the function is to update its coordinates on board'''

# ------------------------------------------------------------------------------------
class Cloud(Board):

    def __init__(self,height,width):
        super(Cloud, self).__init__(height,width);
        self.cloud_x = []
        self.cloud_y = []
        self.generateclouds()

    def generateclouds(self):

        for i in range(0,40):
            self.cloud_x.append(randint(10,450))
            self.cloud_y.append(randint(0,10))

    def shape(self,b):
        row = [[] for i in range(0,3)]
        row[0] = [sp, sp, ' ', sp, sp]
        row[1] = [sp, ' ', sp, ' ', ' ']
        row[2] = [' ', ' ', ' ', ' ', ' ']

        for i in range(0,40):
            for j in range(0,3):
                for k in range(0,5):
                    b.board[self.cloud_y[i]+j][self.cloud_x[i]+k] = cl.colors['Gray']+row[j][k]+cl.colors['brk']

# ------------------------------------------------------------------------------------

class Mario:

    def __init__(self):
        self.w = 0
        self.x = 20
        self.y = 30
        self.isjump = False
        self.temp = 0
        self.origin = True
        self.walk = False
        self.brickjump = False
        self.tp = 0
        self.ju = False
        self._p = self.x
        self.spring = False

    def spawn(self,b,a):
        temp = cl.colors['non'] + '*' + cl.colors['brk']
        matrix = [[] for i in range(3)];
        matrix[0] = [temp,temp]
        matrix[1] = ['#','#']
        if a==1:
            matrix[2] = ['/','\\']
        else :
            matrix[2] = ['\\','/']

        for i in range(0,3):
            for j in range(0,2):
                b.board[self.y-i][self.x+j] = cl.colors['Purple'] + matrix[2-i][j] + cl.colors['brk']

    def respawn(self,b):
        self.y -= 2
        self.temp += 2
        self.origin = True


    def prevclear(self,b):
        matrix = [[] for i in range(3)];
        matrix[0] = [sp,sp]
        matrix[1] = [sp,sp]
        matrix[2] = [sp,sp]
        for i in range(0,3):
            for j in range(0,2):
                b.board[self.y-i][self.x+j] =  matrix[2-i][j]
    '''function for jumping'''
    def jump(self,b):
        if self.isjump:
            if self.temp < 9:
                b.board[self.y][self.x+1] = sp
                b.board[self.y][self.x] = sp
                self.temp = self.temp + 1
                self.y = self.y - 1
                self.spawn(b,1)
            elif self.temp>=9 and self.temp<18 :
                b.board[self.y-2][self.x+1] = sp
                b.board[self.y-2][self.x] = sp
                self.y = self.y + 1
                self.spawn(b,1)
                self.temp = self.temp +1
                if self.temp == 18:
                    self.isjump = False
                    self.temp = 0
    ''' spring function for jumping '''
    def spri(self,b):
        if self.spring:
            if self.temp < 16:
                b.board[self.y][self.x+1] = sp
                b.board[self.y][self.x] = sp
                self.temp = self.temp + 1
                self.y = self.y - 1
                self.spawn(b,1)
            elif self.temp>=16 and self.temp<32 :
                b.board[self.y-2][self.x+1] = sp
                b.board[self.y-2][self.x] = sp
                self.y = self.y + 1
                self.spawn(b,1)
                self.temp = self.temp +1
                if self.temp == 32:
                    self.spring = False
                    self.temp = 0

    ''' function to see if mario is on correct level or not '''
    def orig(self,b):
        if self.origin != True:
            b.board[self.y-2][self.x+1] = sp
            b.board[self.y-2][self.x] = sp
            self.y = self.y + 1
            self.spawn(b, 1)
            self.temp = self.temp - 1
            if self.temp == 0:
                self.origin = True
    '''function to walk over the bricks'''
    def walkoverbricks(self,b):
        if self.walk == True:
            self.origin = True
            self.isjump = False
            self.ju = True
        var = b.emptybelow(self.x, self.y)
        if self.brickjump == True:
            self.walk == False
            if self.tp <7:
                b.board[self.y][self.x+1] = sp
                b.board[self.y][self.x] = sp
                self.tp = self.tp + 1
                self.y = self.y - 1
                self.spawn(b,1)
            elif self.tp>=7 and self.tp<14:
                b.board[self.y-2][self.x+1] = sp
                b.board[self.y-2][self.x] = sp
                self.y = self.y + 1
                self.spawn(b,1)
                self.tp = self.tp +1
                if self.tp == 14:
                    self.tp = 0
                    self.brickjump = False


        elif var =='empty' and self.walk == True:
            if self.temp != 18:
                b.board[self.y-2][self.x+1] = sp
                b.board[self.y-2][self.x] = sp
                self.y = self.y + 1
                self.spawn(b,1)
                self.temp = self.temp +1
                if self.temp == 18:
                    self.temp = 0
                    self.walk = False
# ------------------------------------------------------------------------------------
    def movemario(self, b, t, brick):
        ''' moves Mario'''
        def alarmhandler(signum, frame):
            ''' input method '''
            raise AlarmException

        def user_input(timeout=0.1):
            ''' input method '''
            signal.signal(signal.SIGALRM, alarmhandler)
            signal.setitimer(signal.ITIMER_REAL, timeout)
            try:
                text = getChar()()
                signal.alarm(0)
                return text
            except AlarmException:
                pass
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
            return ''

        char = user_input()
        # self.w = (self.w + 0.1)
        '''inputs'''
        if char == 'q':
            sys.exit()

        if char == 'd':

            touch = False
            for i in range(0,len(brick)):
                if b.stop(self.x,self.y,brick[i]):
                    touch = True
                    # sys.exit()
            var = b.detectcollision(self.x,self.y)
            if self.w<300:
                self.w = self.w + 2
            else:
                if touch==False:
                    self.prevclear(b)
                    if self.x <480:
                        self.x = self.x + 1
            if self.x < 480 and (self.x -self.w<60) and var =='empty':
                if touch==False:
                    self.prevclear(b)
                    self.x = self.x + 3
            elif self.x<480 and self.x - self.w >=60 and var =='empty':
                if touch==False:
                    self.prevclear(b)
                    self.x = self.x + 2
            self.spawn(b,1)


        if char == 'a':
            if self.w>0:
                self.w = self.w - 2
            if self.x >20 and (self.x-self.w > 20):
                self.prevclear(b)
                self.x = self.x -3
                self.spawn(b,0)
            elif self.x >20 and (self.x-self.w <= 20):
                self.prevclear(b)
                self.x = self.x -2
                self.spawn(b,0)

        if char == 'w':
            temp = self.y
            if self.y == 30:
                self.isjump = True
            elif self.ju == True:
                self.brickjump = True
# ------------------------------------------------------------------------------------
class Enemy:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.smart = False


    def spawn(self, b):
        matrix = [[] for i in range(0,2)]
        matrix[0] = ['E','E']
        matrix[1] = ['U','U']

        for i in range(0,2):
            for j in range(0,2):
                b.board[self.y-i][self.x+j] = matrix[i][j]

    def update(self,b,t, mario,ov , tame):
        matrix = [[] for i in range(0,2)]
        matrix[0] = ['E','E']
        matrix[1] = ['U','U']

        if(b.detectcollision(self.x,self.y) == 'mario' or b.detectcollision(self.x,self.y-1) == 'mario'):
            game.chnglive(ov,tame)
            mario.spawn(b,1)

        for i in range(0,2):
            for j in range(0,2):
                b.board[self.y-i][self.x+j] = sp

        if self.x < 15 :
            pass
        else:
            self.x = int(self.x - 0.0025)
            for i in range(0,2):
                for j in range(0,2):
                    b.board[self.y-i][self.x+j] = cl.colors['Red'] + matrix[i][j] + cl.colors['brk']

    def supdate(self,b,t,mario, ov, tame):

        matrix = [[] for i in range(0,2)]
        matrix[0] = ['E','E']
        matrix[1] = ['U','U']
        # self.x = self.x - int(2*0.01*t)  smart enemies
        if(b.detectmar(self.x,self.y,mario)):
            game.chnglive(ov,tame)
            mario.spawn(b,1)

        for i in range(0,2):
            for j in range(0,2):
                b.board[self.y-i][self.x+j] = sp

        if self.x < 25 and self.smart == False:
            self.smart = True
        elif self.smart == True:
            self.x = int(self.x + 1)
            for i in range(0,2):
                for j in range(0,2):
                    b.board[self.y-i][self.x+j] = cl.colors['Red'] + matrix[i][j] + cl.colors['brk']
        else:
            self.x = int(self.x - 0.0025)
            for i in range(0,2):
                for j in range(0,2):
                    b.board[self.y-i][self.x+j] = cl.colors['Red'] + matrix[i][j] + cl.colors['brk']



    def clear(self,b):
        for i in range(0,2):
            for j in range(0,2):
                b.board[self.y-i][self.x+j] = sp

# ------------------------------------------------------------------------------------
class S_Enemy(Enemy):

    def __init__(self, x, y):
        super(S_Enemy, self).__init__(x,y)

    def spawn(self,b):
        matrix = [[] for i in range(0,2)]
        matrix[0] = ['*','*']
        matrix[1] = ['*','*']


        for i in range(0,2):
            for j in range(0,2):
                b.board[self.y-i][self.x+j] = cl.colors['Black']+matrix[i][j]+cl.colors['brk']
    def update(self,b,t, mario, ov, tame):
        matrix = [[] for i in range(0,2)]
        matrix[0] = ['*','*']
        matrix[1] = ['*','*']
        if(b.detectmar(self.x,self.y,mario)):
            game.over(ov, tame)
        for i in range(0,2):
            for j in range(0,2):
                b.board[self.y-i][self.x+j] = sp

        if self.x <15:
            pass
        elif self.x - mario.x < 50:
            self.x = self.x - int(2*0.01*t*0.5)
            for i in range(0,2):
                for j in range(0,2):
                    b.board[self.y-i][self.x+j] = cl.colors['Black']+matrix[i][j]+cl.colors['brk']

# ------------------------------------------------------------------------------------
class brick:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.kuchbhi = 0

    def generate(self,b, foo):
        shape = [[] for i in range(0,2)]
        if foo == 0:
            shape[0] = ['<','>']
            shape[1] = ['1','1']
        elif foo == 1:
            shape[0] = ['<','>']
            shape[1] = ['0','0']
        else:
            shape[0] = [sp,sp]
            shape[1] = [sp,sp]



        for i in range(0,2):
            for j in range(0,2):
                b.board[self.y-i][self.x+j] = cl.colors['Yellow']+shape[i][j]+cl.colors['brk']
                b.board[self.y-i][self.x+j+3] = cl.colors['Yellow']+shape[i][j]+cl.colors['brk']

    def update(self, mario, b):

        var = '0'
        for i in range(0,5):
            if b.detectbrick(self.x+i,self.y,mario) =='mario':
                var = '1'
        if var == '1':
            mario.isjump = False
            mario.origin = False
            self.kuchbhi = self.kuchbhi +1
            self.generate(b,self.kuchbhi)

        var2 = '0'
        for i in range(0,5):
            if b.detectstan(self.x+i, self.y-1, mario) == 'stand':
                var2 = '1'
        if var2 == '1':
            mario.walk =True

# ------------------------------------------------------------------------------------
class ebrick(brick):

        def __init__(self, x, y):
            super(ebrick,self).__init__(x,y)

        def generate(self,b):
            shape = [[]for i in range(0,2)]
            shape[0] = ['X', 'X']
            shape[1] = ['X', 'X']


            for i in range(0,2):
                for j in range(0,2):
                    b.board[self.y-i][self.x+j] = cl.colors['Blue']+shape[i][j]+cl.colors['brk']

        def update(self, mario, b, ov, tame):
            shape = [[]for i in range(0,2)]
            shape[0] = ['X', 'X']
            shape[1] = ['X', 'X']
            var = '0'
            # print(b.detect_touch(self.x, self.y,mario),file = f)
            for i in range(0,2):
                if b.detect_touch(self.x, self.y,mario):
                    var = '1'

            if var == '1':
                game.over(ov, tame)

            for i in range(0,2):
                for j in range(0,2):
                    b.board[self.y-i][self.x+j] = cl.colors['Blue']+shape[i][j]+cl.colors['brk']

# ------------------------------------------------------------------------------------

class Coin:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def spawn(self,b):
        shape = [[] for i in range(0,4)]
        shape[0] = [sp, '*', sp]
        shape[1] = ['*', sp, '*']
        shape[2] = ['*', sp, '*']
        shape[3] = [sp, '*', sp]

        for i in range(0,4):
            for j in range(0,3):
                b.board[self.y-i][self.x+j] = cl.colors['Green']+shape[i][j]+cl.colors['brk']

    def col(self,b, mario):
        if b.detectcoin(self.x, self.y,mario) == 1:
            # print(self.x,mario.x,file=f)
            # print("coin detect ho gaya yeay aya ",b.detectcoin(self.x,self.y,mario),self.x,self.y,file =f )
            return 1
        elif b.detectcoin(self.x, self.y-1,mario) == 1:
            return 1
        elif b.detectcoin(self.x, self.y-2,mario) == 1:
            return 1
        elif b.detectcoin(self.x, self.y-3,mario) == 1:
            return 1

        else: return 0

    def clear(self,b):

        for i in range(0,4):
            for j in range(0,3):
                b.board[self.y-i][self.x+j] = sp

# ------------------------------------------------------------------------------------
class pipe:

    def __init__(self,b):
        self.x = 425
        self.y = 30
        self.generate(b)

    def generate(self,b):
        shape =[[]for i in range(0,6)]
        shape[0] = ['_','_','_']
        shape[1] = ['|','|','|']
        shape[2] = ['I','|','T']
        shape[3] = ['O','|','N']
        shape[4] = ['N','O','W']
        shape[5] = ['J','M','P']

        for i in range(0,6):
            for j in range(0,3):
                b.board[self.y-i][self.x+j] = cl.colors['Light Green']+shape[i][j]+ cl.colors['brk'];

    def movelevel(self,level,mario):
        if level <4:
            level+= 1
        else:
            sys.exit()
        mario.x = 20
        mario.y = 30
        mario.w = 0
        mario.isjump = False
        mario.temp = 0
        mario.origin = True
        mario.walk = False
        mario.brickjump = False
        mario.tp = 0
        mario.ju = False

        return level
class spring:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def generate(self, b, mario):
        shape = [[] for i in range(0,4)]
        shape[3] = list("  _____   ")
        shape[2] = list("   \ /    ")
        shape[1] = list("   / \    ")
        shape[0] = list(" /_|__|_\ ")

        if b.det(self.x, self.y, mario):
            mario.spring = True

        for i in range(0,4):
            for j in range(0, len(shape[0])):
                b.board[self.y -i][self.x+j] = cl.colors['Black']+shape[i][j] + cl.colors['brk']

# ------------------------------------------------------------------------------------
class Boss:

    def __init__(self):
        self.x = 390
        self.y = 30
        self.temp = 0

    def spawn(self, b):
        self.temp += 0.00025
        self.y -= int(self.temp)
        if self.y <=25:
            self.y = 30

        boss = [[] for i in range(0, 9)]
        boss[8] = list("                _ ___    ")
        boss[7] = list("    _          _@)@) \   ")
        boss[6] = list("  _/o\_ _ _ _/~`.`...'~\ ")
        boss[5] = list(" / `,'.~,~.~  .   , . ,  ")
        boss[4] = list("( ' _' _ '_` _  '  .     ")
        boss[3] = list(" ~V~ V~ V~ V~ ~\ `   ' . ")
        boss[2] = list("  _/\ /\ /\ /\_/, . ' ,  ")
        boss[1] = list(" < ~ ~ '~`'~'`, .,  .    ")
        boss[0] = list("  \ ' `_  '`_    _    ', ")

        for i in range(0, 9):
            for j in range(0,len(boss[0])):
                b.board[self.y-i][self.x+j]='\x1b[1;32;44m'+ boss[i][j] + cl.colors['brk']

# ------------------------------------------------------------------------------------
class pitfall:
    def __init__(self,x):
        self.y = 31
        self.x = x

    def generate(self,b, mario):

        if b.fall(mario.x, mario.y, self.x):
            mario.origin = False
            mario.temp = 3

        for i in range(0,9):
            for j in range(0,15):
                b.board[self.y+i][self.x+j]= sp
# ------------------------------------------------------------------------------------
