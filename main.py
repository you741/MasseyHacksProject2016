import os
from pygame import *

os.environ['SDL_VIDEO_WINDOW_POS'] = '70,25'
screen = display.set_mode((1200,730))
#====COLOR====#
BLACK  = (0,0,0)
#====IMAGES====#
back1 = image.load("images/background1.png")
#====MC VAR====#
x,y = 600,500
screen.blit(back1,(0,0))
screen.set_clip(Rect(0,0,1200,730))
running = True
hpbar1 = Rect(50,50,450,50)
hpbar2 = Rect(700,50,450,50)
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    kp = key.get_pressed()
    if kp[K_RIGHT] and x < 3000:
        x += 10
    if kp[K_LEFT] and x > 600:
        x -= 10
    screen.blit(back1,(x*-1+600,0))
    draw.rect(screen,(0,255,0),hpbar1)
    draw.rect(screen,(0,255,0),hpbar2)
    display.flip()
quit()
