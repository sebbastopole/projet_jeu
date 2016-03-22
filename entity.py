from utils import *
from ai import *

DEFAULT_ENTITY_SIZE = 10
DEFAULT_MONSTER_SIZE = 5
        
class Entity(object):

    pos = None 
    color = None
    entId = None
    isAlive = True
    size = DEFAULT_ENTITY_SIZE
    
    def __init__(self, entId, pos):
        self.entId = entId
        self.pos = pos
        self.color = rgb()
        
    def move(self,x,y):
        self.pos.move(x,y)
                       
class Monster(Entity):

    ai = None
    game = None
    size = DEFAULT_MONSTER_SIZE
    
    def __init__(self, game, entId, pos):
        Entity.__init__(self,entId,pos)
        self.game = game
        
    def setAI(self, AI_class):
        self.ai = AI_class(self.game,self.entId)
        
    def action(self):
        if self.ai != None:
            self.ai.decide()


        
   
