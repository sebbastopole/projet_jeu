from utils import *

class Level(object):
    
    lines = []
    
    def __init__(self):
        self.basicLevel()
        
    def basicLevel(self): #cadre distant de 100 pixels des bords (en 800x600)
        # 4 coins du cadre:
        up_left = Point(100,100)
        up_right = Point(700,100)
        down_left = Point(100,500)
        down_right = Point(700,500)
        right_angle = Point(600,500)
        d_r_a= Point(425,275)
        d_r_a1= Point(475,325)
        left_angle = Point(200,500)
        d_l_a = point()
        up_angle = Point(400,100)
        down_angle1 = Point(400,500)
        left_angle1 = Point(200,100)
        right_angle1= Point(600,100)
        # 4 lignes du cadre
        self.lines.append(Line(up_right,up_left))
        self.lines.append(Line(up_left,down_left))
        self.lines.append(Line(down_left,down_right))
        self.lines.append(Line(down_right,up_right))
        self.lines.append(Line(right_angle,left_angle))
        self.lines.append(Line(left_angle,up_angle))
        self.lines.append(Line(up_angle,right_angle))
        self.lines.append(Line(down_angle1,left_angle1))
        self.lines.append(Line(left_angle1,right_angle1))
        self.lines.append(Line(right_angle1,down_angle1))

