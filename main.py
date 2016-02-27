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
    if kp[K_RIGHT] and x < 3000:
        x += 10
    if kp[K_LEFT] and x > 600:
        x -= 10
    screen.blit(back1,(x*-1+600,0)) #draws background
    screen.blit(luffy1,(600-width//2,y)) #draws main character

    draw.rect(screen,(0,255,0),hpbar1) #draws the first HP Bar
    draw.rect(screen,(0,255,0),hpbar2) #draws the second HP Bar
    
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
