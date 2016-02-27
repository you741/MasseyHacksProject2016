import os
from pygame import *
from time import *
from moves import *
os.environ['SDL_VIDEO_WINDOW_POS'] = '70,25'
screen = display.set_mode((1200,730))
#====COLOR====#
BLACK  = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
#====IMAGES====#
back1 = image.load("images/background1.png")
luffy1 = transform.smoothscale(image.load("images/luffy1.png"),(242,198))
luffypunchanims = [image.load("images/luffypunchstart.png"),
                   image.load("images/Luffypunch1.png"),
                   image.load("images/Luffypunch2.png"),
                   image.load("images/Luffypunch3.png"),
                   image.load("images/Luffypunch4.png"),
                   image.load("images/luffypunchend.png")]
screen.blit(back1,(0,0))

#====Moves====#
punch = Move( 5, 0, 0.5, 0.6)
kick = Move( 10, 0, 0.7, 0.9)


#====P1 VAR====#
luffy1 = transform.scale(image.load('images/luffy1.png'),(242,198))
x,y = 300,500
width,height = luffy1.get_width(),luffy1.get_height()
punchrect1 = Rect(0,0,280,30)
dir1 = 0 #direction 0 = right; 1 is left
hp1,maxhp1 = 100,100
jumptimer1 = 0
attacktimer1 = 0
luffycurattack = None
#====P2 VAR====#
x2,y2 = 900,500
width2,height2 = 100,100
hp2,maxhp2 = 100,100
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
    if kp[K_d] and x+width < 1200:
        #right move
        nx = x+10
        dir1 = 0
    if kp[K_a] and x > 0:
        #left move
        nx = x-10
        dir1 = 1
    #makes sure we do not collide with enemy
    if not Rect(nx,y,width,height).colliderect(Rect(x2,y2,width2,height2)):
        x = nx
    if kp[K_w] and time() - jumptimer1 > 0.6:
        #jump
        jumptimer1 = time()
    #MOVES OF P1
    if kp[K_e] and luffycurattack == None:
        #punch
        attacktimer1 = time()
        luffycurattack = punch

    if luffycurattack != None:
        if time()-attacktimer1 > luffycurattack.cooldown:
            luffycurattack = None
    if time() - jumptimer1 <= 0.25:
        y -= 20
    elif time() - jumptimer1 <= 0.5:
        y += 20
    else:
        y = 500
    #P2 CONTROLS
    nx2 = x2
    if kp[K_RIGHT] and x2+width2 < 1200:
        nx2 += 10
    if kp[K_LEFT] and x2 > 0:
        nx2 -= 10
    #makes sure we do not collide with enemy
    if not Rect(nx2,y2,width2,height2).colliderect(Rect(x,y,width,height)):
        x2 = nx2
    if kp[K_UP] and time() - jumptimer2 > 0.6:
        jumptimer2 = time()
    if time() - jumptimer2 <= 0.25:
        y2 -= 20
    elif time() - jumptimer2 <= 0.5:
        y2 += 20
    else:
        y2 = 500
    #DRAWING THE BACKGROUND AND CHARACTERS
    screen.blit(back1,(0,0))
    #draws player 1
    o1_1,o1_2 = (False,False) if not dir1 else (True,False) #orientation of direction facing for player 1
    if time() - attacktimer1 < 0.5:
        #attack animation and damage handling
        screen.blit(transform.flip(luffypunchanims[int((time()-attacktimer1)/0.085)],o1_1,o1_2),(x,y))
        if punchrect1.move(x+dir1*(width-punchrect1.width),y).colliderect(Rect(x2,y2,width2,height2)) and time() - damagetimer2 > 0.6:
            hp2 -= 5
            damagetimer2 = time()
    else:
        screen.blit(transform.flip(luffy1,o1_1,o1_2),(x,y))
    draw.rect(screen,BLACK,(x2,y2,width2,height2))#draws player 2
    #limits hp
    hp2 = max(0,hp2)
    hp1 = max(0,hp1)
    #health bars
    draw.rect(screen,RED,Rect(50,50,450,50))
    draw.rect(screen,RED,Rect(700,50,450,50))
    draw.rect(screen,GREEN,Rect(50,50,int(450*(hp1/maxhp1)),50))
    draw.rect(screen,GREEN,Rect(700,50,int(450*(hp2/maxhp2)),50))
    
    display.flip()
font.quit() #deletes font
quit()
