import os
from pygame import *
from time import *

os.environ['SDL_VIDEO_WINDOW_POS'] = '70,25'
display.set_caption("Fight Fighters: The Fightening") #Working title
victory = True
def victory (screen,person):
    start = False
    screen.fill((0,0,0))
    font.init()
    victoryFont = font.SysFont("Arial", 130)
    retryFont = font.SysFont("Arial", 50)
    quote = ["LUFFY WINS!",
            "ZORRO WINS!",
            "Press Enter to play again!"]
    victoryPic = victoryFont.render((quote[person]), True, (255,255,255))
    retryPic = retryFont.render((quote[2]), True, (255,255,255))
    screen.blit(victoryPic,(212, 150))
    screen.blit(retryPic,(340, 400))
    running = True
    while running:
        for e in event.get():
            if e.type == QUIT:
                running = False
        kp = key.get_pressed()
        
        if not kp[K_RETURN]: 
            start = True
        if kp[K_RETURN] and start:
            break
        display.flip()
    return
