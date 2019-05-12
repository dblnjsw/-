from setting import *

import time
#该类用于实例化游戏中所有的物体，level0里的初始化各种物体
#所有物体可分为object（🐕，石头等），字（字又分为动词名词be动词三种）
class gameObject(pygame.sprite.Sprite):
    def __init__(self,tag,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(imFolder+"/"+tag+".jpg").convert()#加载图片
        self.type=None#type只给object加，同于区分
        if tag=='is':
            self.bit=0
        elif tag == 'wo' :
            self.bit=1<<1
        elif tag=='dog' or tag=='gou':
            self.bit=1<<6
        elif tag == 'cat' or tag=='mao':
            self.bit = 1 << 7
        elif tag=='rock' or tag=='shi':
            self.bit=1<<8
        elif tag=='flag' or tag=='qi':
            self.bit=1<<9
        elif tag=='box' or tag=='xiang':
            self.bit=1<<10
        elif tag == 'ying' :
            self.bit=1<<2
        elif tag=='ding':
            self.bit=1<<3
        elif tag == 'tui':
            self.bit = 1 << 4
        elif tag=='si':
            self.bit=1<<5


        if  tag=='dog':
            self.type='object'
        elif tag=='cat':
            self.type='object'
        elif tag=='rock':
            self.type = 'object'
        elif tag=='flag':
            self.type = 'object'
        elif tag=='box':
            self.type = 'object'

        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

    def __del__(self):
        self.rect.x=1500
        self.rect.y=1500
        
class MovingObject(pygame.sprite.Sprite):
    def __init__(self, tag, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imFolder + "/" + tag + ".jpg").convert()  # 加载图片
        self.image.set_colorkey(WHITE)
        self.image.set_alpha(100)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def moving(self, x, y):
        self.rect.x += x
        self.rect.y += y


class MenuObject(pygame.sprite.Sprite):
    # 括号里填（什么图片，初始坐标x，初始坐标y，往哪个轴移动，移动距离（正负均可））
    def __init__(self, tag, x, y, dx):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imFolder + "/" + tag + ".jpg").convert()  # 加载图片
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.acc = 0
        self.vel = 0
        self.f = 0.08  # 阻力
        self.xx = dx

    def update(self):
        self.acc = (self.xx - self.rect.x) / 1000
        if self.vel > 0:
            ac = self.acc - self.f
        else:
            ac = self.acc + self.f

        self.vel += ac
        self.rect.x += self.vel

        


