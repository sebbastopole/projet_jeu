class Point(object):
    #represente une position x et y dans le plan
    
    x=int()
    y=int()
    
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    
    def move(self,x,y):
        self.x += x
        self.y += y
            
    def __str__(self): #affichage d'une position (console) ex: (x:0-y:0)
        return "(x:"+str(self.x)+"-y:"+str(self.y)+")"
        
    def toTuple(self): #retourne un tuple (x,y)
        return (self.x,self.y)
       
class Line(object):
    #represente un segment de droite dans le plan
    
    p1 = Point()
    p2 = Point()
    
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
    def move(self,x,y):
        self.p1.move(x,y)
        self.p2.move(x,y)

class Circle(object):
    #represente un cercle dans le plan
    
    center = Point()
    radius = int()
    
    def __init__(self,center,radius):
        self.center = center
        self.radius = radius
    def move(self,x,y):
        self.center.move(x,y)
