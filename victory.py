import os
from pygame import *
from time import *

os.environ['SDL_VIDEO_WINDOW_POS'] = '70,25'
screen = display.set_mode((1200,730))
display.set_caption("Fight Fighters: The Fightening") #Working title
victory = True
screen.fill((0,0,0))
font.init()
victoryFont = font.SysFont("Arial", 150)
retryFont = font.SysFont("Arial", 50)
quote = ["LUFFY WINS!",
        "ZORRO WINS!",
        "Press Enter to play again!"]
victoryPic = victoryFont.render((quote[0]), True, (255,255,255))
retryPic = retryFont.render((quote[2]), True, (255,255,255))
screen.blit(victoryPic,(212, 150))
screen.blit(retryPic,(340, 400))
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    display.flip()
quit()
