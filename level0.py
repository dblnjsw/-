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
        
class level4:
    def __init__(self):
        # 狗是我（规则）
        self.gou = gameObject('gou', 300, 200)
        self.is1 = gameObject('is', 400, 200)
        self.wo = gameObject('wo', 500, 200)

        # 两个盒子（实体）和狗（实体）
        self.box1 = gameObject('box', 500, 400)
        self.box2 = gameObject('box', 400, 500)
        self.dog = gameObject('dog', 500, 500)

        # 4个石头（实体）和一面旗子（实体）
        self.rock1 = gameObject('rock', 600, 300)
        self.rock2 = gameObject('rock', 800, 300)
        self.rock3 = gameObject('rock', 700, 200)
        self.rock4 = gameObject('rock', 700, 400)
        self.flag = gameObject('flag', 700, 300)

        # 石是定（规则）
        self.shi = gameObject('shi', 900, 600)
        self.is2 = gameObject('is', 1000, 600)
        self.ding = gameObject('ding', 1100, 600)

        # 箱是推（规则）
        self.xiang = gameObject('xiang', 100, 0)
        self.is3 = gameObject('is', 100, 100)
        self.tui = gameObject('tui', 100, 200)

        # 旗是赢（规则）
        self.qi = gameObject('qi', 100, 400)
        self.is4 = gameObject('is', 100, 500)
        self.ying = gameObject('ying', 100, 600)

        # 所有的东西手动放all里
        self.all = [self.gou, self.is1, self.wo,
                    self.box1, self.box2, self.dog,
                    self.rock1, self.rock2, self.rock3, self.rock4, self.flag,
                    self.shi, self.is2, self.ding,
                    self.xiang, self.is3, self.tui,
                    self.qi, self.is4, self.ying]
        self.be = []
        self.verb = []
        self.noun = []
        self.object = []
        self.wall = []
        self.moveHistory = []
        # 自动分类
        for e in self.all:
            if not e.bit:
                self.be.append(e)
            elif e.bit <= 32:
                self.verb.append(e)
            elif e.type == 'object':
                self.object.append(e)
            else:
                self.noun.append(e)
        for x in range(-1, 13):
            for y in range(-1, 8):
                if x == -1 or y == -1 or x == 12 or y == 7:
                    self.wall.append(gameObject('wall', x * 100, y * 100))
        # 用于存储所有规则
        self.allRule = []
