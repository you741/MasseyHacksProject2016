##character class
from pygame import *

class Character ():
    def __init__ (self, anims, sprite, curattack, x,y,width, height, maxenergy, maxhp, jumpspeed):
        self.sprite = sprite
        self.curattack = curattack
        self.anims = anims
        self.width = width
        self.curattack = curattack
        self.height = height
        self.maxenergy = maxenergy
        self.maxhp = maxhp
        self.jumpspeed = jumpspeed
        self.x = x
        self.y = y
        self.hitbox = Rect(x,y,width,height)
        
    def get_instance(self):
        return Character(self.anims,self.sprite,self.curattack,self.x,self.y,self.width,self.height,self.maxenergy,self.maxhp,self.jumpspeed)
