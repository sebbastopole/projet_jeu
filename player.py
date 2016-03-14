from graphics import *

class Position(object):
    #represente une position x et y dans la fenetre
    x=int()
    y=int()
    
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        
    def __str__(self): #affichage d'une position (console) ex: (x:0-y:0)
        return "(x:"+self.x+"-y:"+self.y+")"
        
class Player(object):

    player_id = int() #numero du joueur
    pos = Position() #position du joueur
    isAlive = True #joueur en vie ou non
    circle = None #cercle du joueur
    size = int()
    
    def __init__(self, player_id, size):
        self.player_id = player_id
        self.size = size
        #creation cercle du joueur:
        self.circle = Circle(Point(self.pos.x,self.pos.y),self.size) 
        
    def move(self,x,y): #bouge de cercle du joueur de x et y
        self.circle.move(x,y)
 
