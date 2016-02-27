import os
from pygame import *
from moves import *
from characters import *
from loading import *
from time import *
os.environ['SDL_VIDEO_WINDOW_POS'] = '70,25'
screen = display.set_mode((1200,730))
loadingscreen(screen)
#====COLOR====#
BLACK  = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
#====IMAGES====#
back1 = image.load("images/background1.png")

luffy1 = image.load('images/luffy1.png')


luffyanims = [[image.load("images/ru1.png"),
                 image.load("images/ru2.png"),
                 image.load("images/ru3.png"),
                 image.load("images/ru4.png"),
                 image.load("images/ru5.png")],
               [image.load("images/Luffypunch1.png"),
               image.load("images/Luffypunch2.png"),
               image.load("images/Luffypunch3.png"),
               image.load("images/Luffypunch4.png")],
              [image.load("images/rf1.png"),
               image.load("images/rf2.png"),
               image.load("images/rf3.png")]]

screen.blit(back1,(0,0))

#====Characters====#
##anims, sprite, curattack, x,y,width, height, maxenergy, maxhp, jumpspeed, 
luffy = Character(luffyanims,luffy1,None,0,0,242,198,100,100,0)

#====Moves====#
#damage, energy, time, cooldown, animsindex, dx,dy, width, height
punch = Move( 5, 0, 0.5, 0.6, 1, 0, 10, 280, 30)
kick = Move( 10, 0, 0.5, 0.6, 1, 0, 140, 280, 30)
swing = Move(7, 0, 0.5, 1, 2, 0, 20, 280, 50)


#====P1 VAR====#
player1 = luffy.get_instance()
x,y = 300,500
width,height = player1.width, player1.height
player1.x, player1.y = 300,500
moving = True
#punchrect1 = Rect(0,0,280,30)
dir1 = 0 #direction 0 = right; 1 is left
hp1,maxhp1 = 100,100
energy,maxenergy = 100,100
jumptimer1 = 0
attacktimer1 = 0
player1.curattack = None
#====P2 VAR====#
player2 = luffy.get_instance()
x2,y2 = 900,500
width2,height2 = player2.width, player2.height
player2.x, player2.y = 900,500
moving2 = True
moving = True
#punchrect1 = Rect(0,0,280,30)
dir2 = 0 #direction 0 = right; 1 is left
hp2,maxhp2 = 100,100
energy,maxenergy = 100,100
jumptimer2 = 0
attacktimer2 = 0
player2.curattack = None

x2,y2 = 900,500
width2,height2 = 100,240
hp2,maxhp2 = 100,100
energy,maxenergy = 100,100
jumptimer2 = 0
damagetimer2 = 0
#====ENEMIES====#



#====GAME PLAY FUNCTION====#
#====ANIMATION FUNCTION====#
##def animate(imgs,drawx,drawy,player=1,filler=back1):
##    "animate a picture"
##    for i in imgs:
##        if not player - 1:
##            #if player 1 then we blit the filler relative to x and y
##            screen.set_clip(Rect(drawx,drawy,width,height))
##            screen.blit(filler,(300+x*-1,0))
##            screen.set_clip(None)
##        screen.blit(i,(drawx,drawy))
##        display.flip()
##        sleep(0.1)
font.init() #Starts font
tymeFont = font.SysFont("Arial", 30)
hpbar1 = Rect(50,50,450,50)
hpbar2 = Rect(700,50,450,50)
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    kp = key.get_pressed()
    #P1 CONTROLS
    nx = x #new x
    moving = False
    if kp[K_d] and x+width < 1200:
        #right move
        moving = True
        nx = x+10
        dir1 = 0
    if kp[K_a] and x > 0:
        #left move
        moving = True
        nx = x-10
        dir1 = 1
    #makes sure we do not collide with enemy
    if not Rect(nx,y,width,height).colliderect(Rect(x2,y2,width2,height2)):
        x = nx
    if kp[K_w] and time() - jumptimer1 > 0.6:
        #jump
        jumptimer1 = time()
        
    #MOVES OF P1 setting to attack
    if kp[K_e] and player1.curattack == None:
        #punch
        attacktimer1 = time()
        player1.curattack = punch
    if kp[K_q] and player1.curattack == None:
        #kick
        attacktimer1 = time()
        player1.curattack = kick
    if kp[K_r] and player1.curattack == None:
        #swing
        attacktimer1 = time()
        player1.curattack = swing
    if player1.curattack != None:
        if time()-attacktimer1 > player1.curattack.cooldown:
            player1.curattack = None
    #actual jump movement
    if time() - jumptimer1 <= 0.25:
        y -= 40
    elif time() - jumptimer1 <= 0.5:
        y += 40
    else:
        y = 500
    #P2 CONTROLS
    nx2 = player2.x
    moving2 = False
    if kp[K_RIGHT] and x2+width2 < 1200:
        nx2 += 10
        moving2 = True
        dir2 = 0
    if kp[K_LEFT] and x2 > 0:
        nx2 -= 10
        moving2 = True
        dir2 = 1
    #makes sure we do not collide with enemy
    if not Rect(nx2,y2,width2,height2).colliderect(Rect(x,y,width,height)):
        player2.x = nx2
    if kp[K_UP] and time() - jumptimer2 > 0.6:
        jumptimer2 = time()
    if time() - jumptimer2 <= 0.25:
        player2.y -= 20
    elif time() - jumptimer2 <= 0.5:
        player2.y += 20
    else:
        player2.y = 500
    #DRAWING THE BACKGROUND AND CHARACTERS
    screen.blit(back1,(0,0))
    o1_1,o1_2 = (False,False) if not dir1 else (True,False) #orientation of direction facing for player 1

    if player1.curattack != None and time() - attacktimer1 < player1.curattack.time:
        #attack animation and damage handling
        screen.blit(transform.flip(player1.anims[player1.curattack.animsindex][int((time()-attacktimer1)/(player1.curattack.time/len(player1.anims[player1.curattack.animsindex])+0.01))],o1_1,o1_2),(x,y))
        #following if statement checks if enemy collides with player1.'s current attack rect
        punchrect1 = player1.curattack.hitbox
#            draw.rect(screen,BLACK,punchrect1.move(x+dir1*(width-punchrect1.width),y+10),1)
        if punchrect1.move(x+dir1*(width-punchrect1.width),y+10).colliderect(Rect(x2,y2,width2,height2)) and time() - damagetimer2 > 0.6:
            hp2 -= player1.curattack.damage
            damagetimer2 = time()
            
    elif moving:
        screen.blit(transform.flip(player1.anims[0][int(time()%0.5/0.1)],o1_1,o1_2),(x,y))
    else:
        screen.blit(transform.flip(player1.sprite,o1_1,o1_2),(x,y))

        
    #draws player 2
    o2_1,o2_2 = (False,False) if not dir2 else (True,False) #orientation of direction facing for player 2

    if player2.curattack != None:
        if time() - attacktimer2 < player2.curattack.time:
            #attack animation and damage handling
            screen.blit(transform.flip(player2.anims[player2.curattack.animsindex][int((time()-attacktimer2)/(player2.curattack.time/len(player2.anims[player2.curattack.animsindex])+0.01))],o2_1,o2_2),(player2.x,player2.y))
            #following if statement checks if enemy collides with player1.'s current attack rect
            punchrect2 = player2.curattack.hitbox
#            draw.rect(screen,BLACK,punchrect1.move(x+dir1*(width-punchrect1.width),y+10),1)
            if punchrect2.move(x+dir2*(width-punchrect1.width),y+10).colliderect(player1.hitbox) and time() - damagetimer1 > 0.6:
                hp1 -= player2.curattack.damage
                damagetimer1 = time()
    elif moving2:
        screen.blit(transform.flip(player2.anims[0][int(time()%0.5/0.1)],o2_1,o2_2),(player2.x,player2.y))
    else:
        screen.blit(transform.flip(player2.sprite,o2_1,o2_2),(player2.x,player2.y))


        
    #limits hp
    hp2 = max(0,hp2)
    hp1 = max(0,hp1)
    #health bars
    draw.rect(screen,RED,Rect(50,50,450,50))
    draw.rect(screen,RED,Rect(700,50,450,50))
    draw.rect(screen,GREEN,Rect(50,50,int(450*(hp1/maxhp1)),50))
    draw.rect(screen,GREEN,Rect(700,50,int(450*(hp2/maxhp2)),50))
    #energy bars
    draw.rect(screen,RED,Rect(50,100,450,50))
    draw.rect(screen,RED,Rect(700,100,450,50))
    
    display.flip()
font.quit() #deletes font
quit()
