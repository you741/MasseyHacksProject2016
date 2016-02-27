import os
from pygame import *
from time import *
os.environ['SDL_VIDEO_WINDOW_POS'] = '70,25'
screen = display.set_mode((1200,730))
#====COLOR====#
BLACK  = (0,0,0)
#====IMAGES====#
back1 = image.load("images/background1.png")
luffy1 = transform.smoothscale(image.load("images/luffy1.png"),(242,198))
#====P1 VAR====#
x,y = 600,500
width,height = luffy1.get_width(),luffy1.get_height()
screen.blit(back1,(0,0))
jumptimer1 = 0
#====P2 VAR====#
x2,y2 = 3000,500
width,height = 100,100
jumptimer2 = 0
#====ENEMIES====#

#====GAME PLAY FUNCTION====#
running = True
hpbar1 = Rect(50,50,450,50)
hpbar2 = Rect(700,50,450,50)
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    kp = key.get_pressed()
    #P1 CONTROLS
    if kp[K_d] and x < 3000:
        x += 10
    if kp[K_a] and x > 600:
        x -= 10
    if kp[K_w] and time() - jumptimer1 > 0.6:
        jumptimer1 = time()
    if time() - jumptimer1 <= 0.25:
        y -= 5
    elif time() - jumptimer1 <= 0.5:
        y += 5
    else:
        y = 500
    #P2 CONTROLS
    if kp[K_RIGHT] and x2 < 3000:
        x2 += 10
    if kp[K_LEFT] and x2 > 600:
        x2 -= 10
    if kp[K_UP] and time() - jumptimer2 > 0.6:
        jumptimer2 = time()
    if time() - jumptimer2 <= 0.25:
        y2 -= 5
    elif time() - jumptimer2 <= 0.5:
        y2 += 5
    else:
        y2 = 500
        
    #P1 SIDE
    screen.set_clip(Rect(0,0,600,730))
    screen.blit(back1,(x*-1+300,0)) #draws background for char 1
    screen.blit(luffy1,(300-width//2,y)) #draws player 1
    #P2 SIDE
    screen.set_clip(Rect(600,0,600,730))
    screen.blit(back1,(x2*-1+900,0)) #draws background for char 2
    draw.circle(screen,BLACK,(900,y2),10)#draws player 2
    screen.set_clip(None)
    #health bars
    draw.rect(screen,(0,255,0),hpbar1)
    draw.rect(screen,(0,255,0),hpbar2)
    display.flip()
quit()
