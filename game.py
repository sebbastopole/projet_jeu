from entity import *
from level import *
import time

class Game(object):
    
    ui = None
    level = None
    players = {}
    npcs = {}
    
    def __init__(self,ui):
        self.ui = ui
        self.level = Level(ui.MODE)
        self.players[0]=Entity(0,Point((self.level.PAS_X/2)*15,300))
        self.players[1]=Entity(1,Point((self.level.PAS_X/2)*15,300))
        self.npcs[0] = Monster(self,0,Point(self.level.PAS_X/2,200))
        self.npcs[0].setAI(BasicAI)
        
    def start(self):
        for npc in self.npcs.values():
            npc.start()
                
