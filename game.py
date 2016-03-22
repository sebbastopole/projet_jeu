from threading import Thread
from entity import *
from level import *
import time

class Game(Thread):
    
    ui = None
    level = None
    players = {}
    npcs = {}
    
    def __init__(self,ui):
        Thread.__init__(self)
        self.ui = ui
        self.level = Level(ui.MODE)
        self.players[0]=Entity(0,Point((self.level.PAS_X/2)*15,300))
        self.players[1]=Entity(1,Point((self.level.PAS_X/2)*15,300))
        self.npcs[0] = Monster(self,0,Point(self.level.PAS_X/2,200))
        self.npcs[0].setAI(BasicAI)
        
    def run(self):
        while self.ui.in_game:
            for npc in self.npcs.values():
                #self.ui.eraseMonster(npc)
                npc.action()
                self.ui.drawMonster(npc)
            time.sleep(5)
                
