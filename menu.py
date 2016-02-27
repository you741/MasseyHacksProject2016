import os
from pygame import *
from time import *

os.environ['SDL_VIDEO_WINDOW_POS'] = '70,25'
screen = display.set_mode((1200,730))
display.set_caption("Fight Fighters: The Fightening") #Working title

menu = True #keeps menu open
arrow = transform.scale(image.load("images/arrow.png"), (100,50))
font.init() #starts font
init() #starts music
regularFont = font.SysFont("Arial", 100)
optionFont = font.SysFont("Arial", 50)
helpFont = font.SysFont("Arial", 25)
quote = ["Paused",
         "Resume",
         "Volume",
         "Use the Arrow keys to move the options.",
         "Press Enter to select a change.",
         "Press Backspace to leave.",
         "Created by:",
         "PLACEHOLDER, PLACEHOLDER,",
         "PLACEHOLDER, PLACEHOLDER"]
spotn = [1,2] #keeps track of the spot, (spot number)
spotp = [(500,300),(500,400)] #position of spot
aspot = [(400,300),(400,400)]
currentarrow = aspot[0] 
currentspotn = spotn[0] #current spot
currentspotp = spotp[0]

regular1Pic = regularFont.render((quote[0]), True, (255,255,255))
regular2Pic = optionFont.render((quote[1]), True, (255,255,255))
regular3Pic = optionFont.render((quote[2]), True, (255,255,255))
help1Pic = helpFont.render((quote[3]), True, (255,255,255))
help2Pic = helpFont.render((quote[4]), True, (255,255,255))
help3Pic = helpFont.render((quote[5]), True, (255,255,255))
credit1Pic = helpFont.render((quote[6]), True, (255,255,255))
credit2Pic = helpFont.render((quote[7]), True, (255,255,255))
credit3Pic = helpFont.render((quote[8]), True, (255,255,255))

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    kp = key.get_pressed()
    if menu:
        screen.fill((0,0,0,100))
        screen.blit(regular1Pic, (450,50))
        screen.blit(regular2Pic, spotp[0])
        screen.blit(regular3Pic, spotp[1])
        screen.blit(help1Pic,(50,600))
        screen.blit(help2Pic,(50,625))
        screen.blit(help3Pic,(50,650))
        screen.blit(credit1Pic,(650,600))
        screen.blit(credit2Pic,(650,625))
        screen.blit(credit3Pic,(650,650))
        screen.blit(arrow,currentarrow)
        if kp[K_BACKSPACE]:
            menu = False #closes menu
        if kp[K_DOWN]:
            if currentspotn == 1:
                currentspotn = spotn[1]
                currentspotp = spotp[1]
                currentarrow = aspot[1]
        if kp[K_UP]:
            if currentspotn == 2:
                currentspotn = spotn[0]
                currentspotp = spotp[0]
                currentarrow = aspot[0]
        if kp[K_RETURN]:
            if currentspotn == 1:
                menu = False
            if currentspotn == 2:
                mixer.music.stop()
            if currentspotn == 2:
                #NEED TO LOAD SONG FIRST#
                mixer.music.play()
    else:
        #CODE#
        pass
    display.flip()
font.quit()
quit()
