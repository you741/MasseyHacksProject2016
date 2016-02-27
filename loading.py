import os
from pygame import *

os.environ['SDL_VIDEO_WINDOW_POS'] = '70,25'
screen = display.set_mode((1200,730))
display.set_caption("Fight Fighters: The Fightening") #Working title

screen.fill((0,0,0))
loading = True
font.init()
titleFont = font.SysFont("Arial", 150)
subtitleFont = font.SysFont("Arial", 100)
startFont = font.SysFont("Arial",40)
quote = ["FIGHT FIGHTERS",
         "THE FIGHTENING!",
         "Press Enter to continue!"]
titlePic = titleFont.render((quote[0]), True, (255,255,255))
subtitlePic = subtitleFont.render((quote[1]), True, (255,255,255))
startPic = startFont.render((quote[2]), True, (255,255,255))

screen.blit(titlePic,(100, 150))
screen.blit(subtitlePic,(250, 300))
screen.blit(startPic,(425, 600))

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    kp = key.get_pressed()
    if loading:
        if kp[K_RETURN]:
            loading = False
    else:
########ADD CODE#########
    display.flip()
font.quit()
quit()
