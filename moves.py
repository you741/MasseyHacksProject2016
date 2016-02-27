##handling
from pygame import *
class Move:    
    def __init__ (self, damage, energy, time, cooldown, animsindex, dx,dy, width, height):
        self.damage = damage
        self.energy = energy
        self.time = time
        self.cooldown = cooldown
        self.animsindex = animsindex
        hitbox = Rect(dx,dy,width,height)
        self.hitbox = hitbox
