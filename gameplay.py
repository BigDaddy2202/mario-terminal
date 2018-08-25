''' this module is for managing score and ending game'''
import sys
from os import system
from time import sleep
import colors as cl


#-----------------------------------------------------------------------------------------------------
class Gameplay:
    def __init__(self):
        self.score = 0
        self.lives = 10

    ''' this is top navigation bar '''
    def topnav(self):
        print("score: ",self.score,"\t\t\tlives: ",int(self.lives/2))
        print("")
# -------------------------------------------------------------------------------------------------
    '''function is called whenever something happens whhich may alter the score'''
    def change(self, dest):
        if dest == 'brick0':
            self.score += 100
        if dest == 'brick1':
            self.score += 50
        if dest == 'en':
            self.score += 20
        if dest == 'sen':
            self.score += 50
        if dest == 'boss':
            self.score += 500
        if dest == 'coin':
            self.score += 30

    def chnglive(self,b,t):

        if self.lives <= 0:
            system('clear')
            self.over(b,t)
        else:
            self.lives -= 1
# --------------------------------------------------------------------------------------------------

    '''these last two functions to just provide an interface end the game'''
    def over(self,b,t):

        matrix = [[] for i in range(0,5)]

        matrix[4] = list(" ,---.  ,--,--.,--,--,--.,---.      ,---.,--.  ,--.,---. ,--.--. ")
        matrix[3] = list("| .-. |' ,-.  ||        | .-. :    | .-. |\  `'  /| .-. :|  .--' ")
        matrix[2] = list("' '-' '\ '-'  ||  |  |  \   --.    ' '-' ' \    / \   --.|  |    ")
        matrix[1] = list(".`-  /  `--`--'`--`--`--'`----'     `---'   `--'   `----'`--'    ")
        matrix[0] = list("`---'                                                            ")



        for i in range(0,5):
            for j in range(0,len(matrix[0])):
                b.board[20 -i][40+j] = '\x1b[0;31;44m'+matrix[i][j]+cl.colors['brk']

        b.printb(0)
        sleep(2)
        self.end(t)
# ---------------------------------------------------------------------------------------------------
    def end(self, t):

        system('clear')
        print("final score: ",int(self.score + (500-t)))
        print("final time: ",int(t))
        sleep(2)
        sys.exit()
# ----------------------------------------------------------------------------------------------------
