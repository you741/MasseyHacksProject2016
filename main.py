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
luffy1 = transform.scale(image.load('images/luffy1.png'),(242,198))
#====MC VAR====#
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
font.init() #Starts font
tymeFont = font.SysFont("Arial", 30)
hpbar1 = Rect(50,50,450,50)
hpbar2 = Rect(700,50,450,50)
tyme = 100
running = True
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
    screen.blit(back1,(x*-1+600,0)) #draws background
    screen.blit(luffy1,(600-width//2,y)) #draws main character

    draw.rect(screen,(0,255,0),hpbar1) #draws the first HP Bar
    draw.rect(screen,(0,255,0),hpbar2) #draws the second HP Bar

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
    screen.blit(luffy1,(600-width//2,y))

    tyme -= 1
    tyme = str(tyme)
    tymePic = tymeFont.render((tyme), True, (0,0,0))
    screen.blit(tymePic,(650,50))
    tyme = int(tyme)
    
    display.flip()
font.quit() #deletes font
del tymeFont
quit()
