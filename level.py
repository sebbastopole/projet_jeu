from utils import *

class Level(object):
    
    lines = []
    
    def __init__(self):
        self.basicLevel()
        
    def basicLevel(self): #cadre distant de 100 pixels des bords (en 800x600)
        # 4 coins du cadre:
        up_right = Point(100,100)
        up_left = Point(700,100)
        down_right = Point(100,500)
        down_left = Point(700,500)
        # 4 lignes du cadre
        self.lines.append(Line(up_right,up_left))
        self.lines.append(Line(up_left,down_left))
        self.lines.append(Line(down_left,down_right))
        self.lines.append(Line(down_right,up_right))

