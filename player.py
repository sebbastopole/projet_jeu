from graphics import *

class Position(object):

    x=int()
    y=int()
    
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "(x:"+self.x+"-y:"+self.y+")"
        
class Player(object):

    player_id = int()
    pos = Position()
    isAlive = True
    circle = None
    size = int()
    
    def __init__(self, player_id, size=10):
        self.player_id = player_id
        self.circle = Circle(Point(self.pos.x,self.pos.y),self.size)
    def move(self,x,y):
        self.circle.move(x,y)
    
