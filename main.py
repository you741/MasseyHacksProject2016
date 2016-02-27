import os
from pygame import *

os.environ['SDL_VIDEO_WINDOW_POS'] = '70,25'
screen = display.set_mode((1200,730))
#====COLOR====#
BLACK  = (0,0,0)
#====IMAGES====#
back1 = image.load("images/background1.png")
luffy1 = transform.scale(image.load('images/luffy1.png'),(242,198))
#====MC VAR====#
x,y = 600,500
width,height = luffy1.get_width(),luffy1.get_height()
screen.blit(back1,(0,0))
screen.set_clip(Rect(0,0,1200,730))
running = True
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
    screen.blit(luffy1,(600-width//2,y))
    display.flip()
quit()
