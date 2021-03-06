from utils import *
import random

class Level(object):
    
    PAS_X = 50
    lines = []
    w=None
    h=None
    
    def __init__(self,dim):
        self.w = dim[0]
        self.h = dim[1]
        self.labyrinthe()
        
    def labyrinthe(self):
        self.frame()
        var = self.PAS_X
        while var <= self.w-self.PAS_X:
            self.wall(var)
            var+=self.PAS_X
        self.wall2()
        
    def frame(self):
        up_left = Point (0,0)
        up_right = Point (self.w,0)
        down_left = Point (0,self.h)
        down_right =Point (self.w,self.h)
        self.lines.append(Line(up_right,up_left))
        self.lines.append(Line(up_left,down_left))
        self.lines.append(Line(down_left,down_right))
        self.lines.append(Line(down_right,up_right))
        
    def wall2(self):
        for elem in self.lines:
            print elem.p1,elem.p2
            if elem.p1.y!= 0 and elem.p2.y!=self.h:
                if elem.p2.y!= 0 and elem.p1.y!=self.h:
                    if elem.p1.y != elem.p2.y:
                        barriere=random.random()
                        if barriere<=0.25:
                            nextpoint=Point(elem.p1.x+self.PAS_X,elem.p1.y)
                            if collides(Circle(nextpoint,1),self.lines):
                                self.lines.append(Line(elem.p1,nextpoint))
                        elif 0.25<barriere and barriere<=0.5:
                            nextpoint=Point (elem.p1.x-self.PAS_X,elem.p1.y)
                            if collides(Circle(nextpoint,1),self.lines):
                                self.lines.append(Line(elem.p1,nextpoint))
                        elif 0.5<barriere and barriere<=0.75:
                            nextpoint=Point (elem.p1.x+self.PAS_X,elem.p2.y)
                            if collides(Circle(nextpoint,1),self.lines):
                                self.lines.append(Line(elem.p2,nextpoint))
                        elif 0.75<barriere and barriere<=1.0:
                            nextpoint=Point (elem.p1.x-self.PAS_X,elem.p2.y)
                            if collides(Circle(nextpoint,1),self.lines):
                                self.lines.append(Line(elem.p2,nextpoint))
    def wall (self,var):
        point=Point(var,0)
        point2=Point(var,self.h)
        f = 1
        while point.y < point2.y - self.PAS_X:#tant que courant <bas
            reste= self.h-point.y
            l=self.h-point.y-self.PAS_X-(f*self.PAS_X*3)
            o=self.h-reste+self.PAS_X
            r=int(random.random()*l)+o
            point1=Point(var,r)
            if point1.y<=point2.y-self.PAS_X*3:
                self.lines.append(Line(point,point1))
            else:
                self.lines.append(Line(point,point2))# ajout ligne de courant jusque en bas
            point = Point(var,point1.y+self.PAS_X)#courant= plus bas de PAS_X
            
            
