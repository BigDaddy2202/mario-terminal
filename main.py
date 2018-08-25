import sys
from threading import Timer
from board import Board
from time import sleep,time
from random import randint
import objects
from os import system,name
# ------------------------------------------------------------------------------------
'''for debugging '''
# f=open('debug.txt', 'w')
def clear():
    system('clear')

print("welcome to assignment Mario\n")
lev = int(input("Enter the level number: [1, 2, 3, 4]: "))

if lev not in [1, 2, 3, 4]:
    lev = 1

''' debugging statements'''
# print(lev,file=f)
# ------------------------------------------------------------------------------------

def start(level):
    '''declaring all the objects and spawning them before game start'''
# ------------------------------------------------------------------------------------
    h,w = 40,500
    enemies = []
    bricks = []
    coins =[]
    pipe = []
    springs = []
    bd = Board(h, w)
    over = Board(h, w)
    pipe.append(objects.pipe(bd))
    protag = objects.Mario()
    clouds = objects.Cloud(h,w)
    clouds.shape(bd)
    protag.spawn(bd,1)
    run,t = True,0
    springs.append(objects.spring(25, 30))
    if level ==4 : springs.append(objects.spring(375, 30))
    for i in range(0, 3 + 6*level):
        enemies.append(objects.Enemy(randint(200,365),30))
        enemies[i].spawn(bd)
    for i in range(0,6 + 7*level):
        bricks.append(objects.brick(randint(50,365),25))
        bricks[i].generate(bd, 0)
    for i in range(0,5 + 3 *level):
        coins.append(objects.Coin(randint(50,365),23))
        coins[i].spawn(bd)
    for i in range(0,len(springs)):
        springs[i].generate(bd,protag)

    if level >= 2 :
        smart = []
        for i in range(0,2 + 2*level):
            smart.append(objects.S_Enemy(randint(300,380),30))
            smart[i].spawn(bd)
    if level >= 3 :
        ebricks = []
        for i in range(0, 6 + level):
            ebricks.append(objects.ebrick(randint(100, 365), 21))
            ebricks[len(ebricks)-1].generate(bd)
        pits = objects.pitfall(70)

    if level == 4:
        pit2 = objects.pitfall(300)
        boss = objects.Boss()
# ------------------------------------------------------------------------------------
    stime = time()
    '''running the game'''
    while run:

        if level == 4:
            if bd.die(protag.x,protag.y)== True:
                objects.game.over(over, curr-stime)  # for game over
        curr= time()
        if protag.y>30:
            objects.game.over(over, curr-stime)
        t += 1
        '''detectint each collision'''
        for i in range(len(enemies)-1, -1, -1):
            var = bd.destroy(enemies[i].x, enemies[i].y,protag)
            if( var != 'kill'):
                if level <=2:
                    enemies[i].update(bd, t, protag, over, curr-stime)
                else:
                    enemies[i].supdate(bd, t, protag, over, curr-stime)
            elif enemies[i].x<15:
                enemies[i].clear(bd)
                del enemies[i]

            elif enemies[i].x>450:
                del enemies[i]
            else:
                objects.game.change('en')
                enemies[i].clear(bd)
                del enemies[i]

        for i in range(len(coins)-1,-1,-1):
            if coins[i].col(bd, protag)== 1:
                objects.game.change('coin')
                coins[i].clear(bd)
                protag.spawn(bd,1)
                del coins[i]

        for i in range(len(bricks)-1,-1,-1):
            bricks[i].update(protag, bd)
            if bricks[i].kuchbhi == 1: objects.game.change('brick1')
            if bricks[i].kuchbhi>=2:
                objects.game.change('brick0')
                del bricks[i]

        for i in range(0,len(springs)):
            springs[i].generate(bd,protag)

        if(level>=2):
            for i in range(len(smart)-1,-1,-1):
                smart[i].update(bd,t,protag, over, curr-stime)

        if(level >= 3):
            for i in range(len(ebricks)-1,-1,-1):
                ebricks[i].update(protag,bd, over, curr-stime)
        if(level == 4):
            pit2.generate(bd,protag)
            boss.spawn(bd)
        '''after checking collisions spawning objects with new co ordinates'''
        if level >=3 :
            pits.generate(bd,protag)
        bd.printb(int(protag.w))
        protag.movemario(bd, t,pipe)
        protag.walkoverbricks(bd)
        protag.spri(bd)
        protag.jump(bd)
        protag.orig(bd)
        '''increasing the level'''
        if bd.detpip(protag.x, protag.y, pipe[0]) == 'proceed':
            level = pipe[0].movelevel(level, protag)
            if(level>4):
                clear()
                objects.game.end(curr -stime)
            start(level)

        sleep(0.01)

start(lev)
