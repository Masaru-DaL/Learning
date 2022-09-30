import pygame
from pygame.locals import Rect

# パドルクラス
class Paddle:

    PADDLE_COLOR = (242, 180, 0)
    PADDLE_RECT_X = 10  # 後に300 に変える
    PADDLE_RECT_Y = 700
    PADDLE_RECT_WIDTH = 580  # 後に100 に変える
    PADDLE_RECT_HEIGHT = 30
    PADDLE_MOVE_X = 10

    # コンストラクタ
    def __init__(self):
        # 色、描画用の矩形を設定
        self.col = Paddle.PADDLE_COLOR
        self.rect = Rect(
            Paddle.PADDLE_RECT_X,
            Paddle.PADDLE_RECT_Y,
            Paddle.PADDLE_RECT_WIDTH,
            Paddle.PADDLE_RECT_HEIGHT,
        )

    # 移動処理
    def move(self, dir):
        pass

    # 描画処理
    def draw(self, surface):
        pygame.draw.rect(surface, self.col, self.rect)
