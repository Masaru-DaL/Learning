import random
import math
import pygame
from pygame.locals import Rect

# ボールクラス
class Ball:

    BALL_COLOR = (242, 242, 0)
    BALL_RECT_X = 300
    BALL_RECT_Y = 400
    BALL_RECT_WIDTH = 20
    BALL_RECT_HEIGHT = 20
    # 初期発射角度の範囲（この場合-25度から25度にする）
    START_DIR_DIFF = 25
    
    # コンストラクタ
    def __init__(self, speed):
        # 色、描画用の矩形、引数でもらったスピードを設定
        self.col = Ball.BALL_COLOR
        self.rect = Rect(Ball.BALL_RECT_X, Ball.BALL_RECT_Y, 
                         Ball.BALL_RECT_WIDTH, Ball.BALL_RECT_HEIGHT)
        self.speed = speed

    # 球の移動処理
    def move(self):
        pass

    # 描画処理
    def draw(self, surface):
        pygame.draw.ellipse(surface, self.col, self.rect)
