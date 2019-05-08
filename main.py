#!C:/python/python.exe
from test import *
from level0 import *

class game:
    def __init__(self):#构造函数，初始化各种东西
        pygame.init()
        pygame.mixer.init()
        self.src = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running=True
        self.upLock=1
        self.moves=[]


        self.allSprite=pygame.sprite.Group()
        #加载关卡
        self.l0=level0()
        for e in self.l0.all:
            self.allSprite.add(e)
    def run(self):#主循环
        while self.running:
            self.update()#很重要！！下面两个方法不重要
            self.draw()
            self.events()
    def update(self):
        #获取键盘
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.moveCommand(-100,0)
            self.upLock=1
        elif keys[pygame.K_RIGHT]:
            self.moveCommand(100,0)
            self.upLock = 1
        elif keys[pygame.K_DOWN]:
            self.moveCommand(0,100)
            self.upLock = 1
        elif keys[pygame.K_UP]:
            self.moveCommand(0,-100)
            self.upLock = 1
        elif keys[pygame.K_z]:
            self.withdraw()
            self.upLock=1
        #每下行动后更新规则，50行的if
        if self.upLock==1:
            self.l0.allRule.clear()
            for e in self.l0.be:
                #寻找名词是动词规则
                for ee in self.l0.verb:
                    #“是”的右边有没有动词
                    if ee.rect.x==e.rect.x+100 and ee.rect.y==e.rect.y:
                        for eee in self.l0.noun:
                            #如果有，那左边有没有名词
                            if eee.rect.x==e.rect.x-100 and eee.rect.y==e.rect.y:
                                if self.l0.allRule.__contains__(ee.bit|eee.bit):
                                    pass
                                else:
                                    self.l0.allRule.append(ee.bit|eee.bit)

                    #“是”的下面有没有动词，同上
                    if ee.rect.y==e.rect.y+100 and ee.rect.x==e.rect.x:
                        for eee in self.l0.noun:
                            # 如果有，那上边有没有名词
                            if eee.rect.y==e.rect.y-100 and eee.rect.x==e.rect.x:
                                if self.l0.allRule.__contains__(ee.bit | eee.bit):
                                    pass
                                else:
                                    self.l0.allRule.append(ee.bit | eee.bit)

                #寻找名词是名词规则
                for ee in self.l0.noun:
                    # “是”的右边有没有名词
                    if ee.rect.x == e.rect.x + 100 and ee.rect.y == e.rect.y:
                        for eee in self.l0.noun:
                            # 如果有，那左边有没有名词
                            if eee.rect.x == e.rect.x - 100 and eee.rect.y == e.rect.y:
                                if self.l0.allRule.__contains__(eee.bit | ee.bit):
                                    pass
                                else:
                                    self.l0.allRule.append(ee.bit | eee.bit)
                                    self.changeObject(eee.bit, ee.bit)
                    #“是”的下面有没有名词，同上
                    if ee.rect.y==e.rect.y+100 and ee.rect.x==e.rect.x:
                        for eee in self.l0.noun:
                            # 如果有，那上边有没有名词
                            if eee.rect.y==e.rect.y-100 and eee.rect.x==e.rect.x:
                                if self.l0.allRule.__contains__(ee.bit | eee.bit):
                                    pass
                                else:
                                    self.l0.allRule.append(ee.bit | eee.bit)
                                    self.changeObject(eee.bit,ee.bit)
            #判断我是不是在赢的物体上，是就结束游戏
            for e in self.l0.allRule:
                if e&1<<2:
                    for ee in self.l0.object:
                        if e&ee.bit:
                            for eee in self.l0.allRule:
                                if eee & 2:
                                    for me in self.l0.object:
                                        if eee & me.bit:
                                            if me.rect.x==ee.rect.x and me.rect.y==ee.rect.y:
                                                self.running=False
            for e in self.l0.allRule:
                if e&1<<5:
                    for ee in self.l0.object:
                        if e&ee.bit:
                            for eee in self.l0.allRule:
                                if eee & 2:
                                    for me in self.l0.object:
                                        if eee & me.bit:
                                            if me.rect.x==ee.rect.x and me.rect.y==ee.rect.y:
                                                me.__del__()


            self.upLock=0
            time.sleep(0.2)
    def draw(self):
        #背景白色
        self.src.fill((255, 255, 255))
        #显示相关
        self.allSprite.draw(self.src)
        pygame.display.flip()
        pass
    def events(self):
        #检测关闭
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.running = False
    #获取键盘按键后，找谁是我
    def moveCommand(self,x,y):
        for e in self.l0.allRule:
            if e&2:
                for ee in self.l0.object:
                    if e&ee.bit:
                        self.move(ee,x,y)
    #movecommand找到谁是我后调用move（）
    def move(self,unit,x,y):
        cm=1
        self.moves.append(unit)#moves列表用于存储一条直线上要移动的物体
        for e in self.l0.all:
            if e.rect.x == unit.rect.x + x and e.rect.y == unit.rect.y + y:#移动方向上的东西
                if not self.l0.object.__contains__(e):#如果e不是物体（就是汉字，可以移动）
                    self.move(e,x,y)#递归，看前面物体的前面有没有物体
                elif self.l0.allRule.__contains__(e.bit|1<<4):#如果当前规则里e是推（1<<4代表推）
                    self.move(e,x,y)
                elif self.l0.allRule.__contains__(e.bit|1<<3):#如果当前规则里e是定（不能推）
                    cm=0
                    break
        for e in  self.l0.wall:
            if e.rect.x == unit.rect.x + x and e.rect.y == unit.rect.y + y:
                cm=0
        #前面没东西了，移动
        if cm:
            #保存移动记录，用于撤回键功能
            lll=[]
            for e in self.moves:
                ll=[e,e.rect.x,e.rect.y]
                lll.append(ll)
            if lll:
                self.l0.moveHistory.append(lll.copy())

            #遍历moves，移动里面每个单位
            for e2 in self.moves:
                e2.rect.x+=x
                e2.rect.y+=y
        self.moves.clear()
    #出现名词是名词的规则后调用
    def changeObject(self,changeFrom,to):
        xx=0
        for e in self.l0.object:
            if e.bit==to:
                xx=e.image
                break
        for e in self.l0.object:
            if e.bit==changeFrom:
                e.image=xx
                e.bit=to
    def withdraw(self):
        if self.l0.moveHistory:
            temp=self.l0.moveHistory.pop()
            for e in temp:
                unit=e[0]
                unit.rect.x=e[1]
                unit.rect.y=e[2]

#程序从这里开始，run是死循环
g = game()
g.run()
pygame.quit()
