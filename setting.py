import pygame
import os

WIDTH = 1200
HEIGHT = 750

allSprite = pygame.sprite.Group()

running = True

gFolder = os.path.dirname(__file__)
imFolder = gFolder + "/img"

# 216add
FONT_NAME = 'SimHei'
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TITLE = 'DOG IS YOU'
FPS = 60
ALL_PICTURE_TAG = [ 'rock', 'flag','grass','box','dog']
INCREASE = 'increase'
DECREASE = 'decrease'
M_Y = 'y'
M_X = 'x'
GO = 1
REVERSE = 2
