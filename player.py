from utils import *
import game_ui
import random
import time
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

class AI(object):
    ui = None
    def __init__(self,ui):
        self.ui=ui
        self.move()
        
    def move(self):
        i=0
        while True:
            #time.sleep(0.01)
            if i%100==0:
                r=0
            if i%100==25:
                r=0.3
            if i%100==50:
                r=0.6
            if i%100==75:
                r=0.9
            i +=1   
            if r<=0.25:
                test_pos = Point(self.ui.p1.pos.x,self.ui.p1.pos.y+5)
                if not collides(Circle(test_pos,self.ui.p1.size),self.ui.level.lines):
                    self.ui.movePlayer(self.ui.p1,0,5)
            if r<=0.5 and r>0.25:
                test_pos = Point(self.ui.p1.pos.x,self.ui.p1.pos.y-5)
                if not collides(Circle(test_pos,self.ui.p1.size),self.ui.level.lines):
                    self.ui.movePlayer(self.ui.p1,0,-5)
            if r<=0.75 and r>0.5:
                test_pos = Point(self.ui.p1.pos.x+5,self.ui.p1.pos.y)
                if not collides(Circle(test_pos,self.ui.p1.size),self.ui.level.lines):
                    self.ui.movePlayer(self.ui.p1,5,0)
            else:
                test_pos = Point(self.ui.p1.pos.x-5,self.ui.p1.pos.y)
                if not collides(Circle(test_pos,self.ui.p1.size),self.ui.level.lines):
                    self.ui.movePlayer(self.ui.p1,-5,0)
