#!C:/python/python.exe
from test import *
from level0 import *
import random

class game:
    def __init__(self):#构造函数，初始化各种东西
        pygame.init()
        pygame.mixer.init()
        self.src = pygame.display.set_mode((WIDTH, HEIGHT),pygame.FULLSCREEN)
        self.running=True
        self.upLock=1
        self.moves=[]
        # 216add
        self.wait_any_key = True
        self.clock = pygame.time.Clock()
        self.timeee = 0

        self.allSprite=pygame.sprite.Group()
        #加载关卡
        self.l0=level4()
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
    def show_start_screen(self):
        # 进入一个等待任意按键的死循环
        fall_picture_queue = []

        test_menu = MenuObject('title', -300, 100,420)
        # hit_size = 22
        # size_up = True
        # 开始界面设置
        while self.wait_any_key:
            #self.clock.tick(FPS)
            self.events()
            self.src.fill(WHITE)
            #self.draw_text(TITLE, 48, BLACK, WIDTH / 2, HEIGHT / 4)
            self.draw_text("操作说明：方向键移动", 22, BLACK, WIDTH / 2, HEIGHT / 2)
            # self.draw_text("按任意键开始", int(hit_size), BLACK, WIDTH / 2, HEIGHT * 3 / 4)
            press_enter = MovingObject('start', WIDTH / 4.5, HEIGHT * 3 / 4)
            temp_sprite = pygame.sprite.Group()
            temp_sprite.add(press_enter)
            test_menu.update()

            temp_sprite.add(test_menu)

            self.timeee=self.timeee+1
            if random.randint(0, 100) >= 95 and self.timeee>=30:
                r_picture = ALL_PICTURE_TAG[random.randint(0, len(ALL_PICTURE_TAG) - 1)]
                r_x = random.randint(0, 12)
                fall_picture_queue.append(MovingObject(r_picture, r_x*100, -100))
                self.timeee=0

            for x in fall_picture_queue:
                temp_sprite.add(x)
                x.moving(0, 2)
            """
            if size_up is True:
                hit_size += hit_size / 64
            else:
                hit_size -= 9 / hit_size
            if hit_size >= 32:
                size_up = False
            elif hit_size <= 18:
                size_up = True
            """
            temp_sprite.draw(self.src)
            pygame.display.flip()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                self.wait_any_key = False
        self.wait_any_key=True

    #选择关卡见面
    def show_select_screen(self):
        self.l1 = MenuObject('level1', -1000, 0, 0)
        self.l2 = MenuObject('level2', -1000, 0, 400)
        self.l3 = MenuObject('level3', -1000, 0, 800)
        self.l4 = MenuObject('level4', -1000, 400, 0)
        self.l5 = MenuObject('level5', -1000, 400, 400)
        temp_sprite=pygame.sprite.Group()
        temp_sprite.add(self.l1)
        temp_sprite.add(self.l2)
        temp_sprite.add(self.l3)
        temp_sprite.add(self.l4)
        temp_sprite.add(self.l5)

        while self.wait_any_key:
            self.events()
            self.src.fill(WHITE)
            temp_sprite.update()
            temp_sprite.draw(self.src)
            pygame.display.flip()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_1]:
                self.wait_any_key = False

    def draw_text(self, text, size, color, x, y):  # 方法：打印文字
        font = pygame.font.Font(pygame.font.match_font(FONT_NAME), size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.src.blit(text_surface, text_rect)
#程序从这里开始，run是死循环
g = game()
g.show_start_screen()
g.show_select_screen()
g.run()
pygame.quit()
