from graphics import *
from utils import Point

DEFAULT_PLAYER_SIZE = 10
        
class Player(object):

    pos = None #position du joueur
    size = DEFAULT_PLAYER_SIZE #taille du joueur
    player_id = int() #numero du joueur
    p_color = None
    isAlive = True #joueur en vie ou non
    
    def __init__(self, player_id, pos):
        self.player_id = player_id
        self.pos = pos
        color = (player_id*100)%255
        self.p_color = (color,color,color)
        
    def move(self,x,y): #bouge la pos du joueur de x et y
        self.pos.move(x,y)
 
