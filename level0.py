from gameObject import *

class level0:
    #关卡布局
    def __init__(self):
        self.gou=gameObject('gou',400,100)
        self.dog=gameObject('dog',100,0)
        self.iss=gameObject('is',500,100)
        self.wo=gameObject('wo',600,100)
        self.shi=gameObject('shi',400,200)
        self.rock1=gameObject('rock',300,400)
        self.rock2 = gameObject('rock', 400, 500)
        self.iss2=gameObject('is',700,100)
        self.ding=gameObject('ding',700,200)
        self.tui=gameObject('tui',700,300)

        self.si=gameObject('si',600,400)
        self.ying=gameObject('ying',600,500)


    #所有的东西手动放all里
        self.all=[self.gou,self.dog,self.iss,self.wo,self.rock1,self.rock2,self.shi,self.iss2,self.ding,self.tui,self.si,self.ying]
        self.be = []
        self.verb = []
        self.noun = []
        self.object = []
        self.wall=[]
        self.moveHistory=[]
    #自动分类
        for e in self.all:
            if not e.bit:
                self.be.append(e)
            elif e.bit<=32:
                self.verb.append(e)
            elif e.type=='object':
                self.object.append(e)
            else:
                self.noun.append(e)
        for x in range(-1,13):
           for y in range(-1,8):
               if x==-1 or y==-1 or x==12 or y==7:
                    self.wall.append(gameObject('wall',x*100,y*100))
    #用于存储所有规则
        self.allRule=[]