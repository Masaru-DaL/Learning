import pygame
from pygame.locals import Rect
from math import radians, sin, cos
from random import randint

# ============ 描画クラス ============
class Drawable:
    
    # コンストラクタ
    def __init__(self, rect):
        self.rect = rect        # 描画する四角
        self.step = [0, 0]      # 移動する量

    # 移動処理
    def move(self):
        pass

# ============ 隕石クラス ============
class Rock(Drawable):

    def __init__(self, level, pos, size, speed):
        super().__init__(Rect(0, 0, size, size))
        self.image = pygame.image.load("image/rock.png")

    # 描画処理
    def draw(self):
        pass

    # １ループ当たりの処理
    def tick(self):
        pass

# ============ 自機クラス ============
class Ship(Drawable):
    
    def __init__(self):
        super().__init__(Rect(355, 370, 90, 60))
        self.image = pygame.image.load("image/ship.png")
        self.bang = pygame.image.load("image/bang.png")

    # 描画処理
    def draw(self):
        pass

    # １ループ当たりの処理
    def tick(self):
        pass

# ============ ショットクラス ============
class Shot(Drawable):
    
    pass
