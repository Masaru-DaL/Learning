from random import randint
import pygame
from pygame.locals import Rect

# ======= 描画クラス =======
class Drawable:

    surface = None  # 描画する対象
    window_size = None  # ウィンドウのサイズ

    # クラスメソッド：ウィンドウ情報の設定
    @classmethod
    def set_window_info(cls, surface, window_size):
        cls.surface = surface  # 描画対象の画面
        cls.window_size = window_size  # 描画対象の画面のサイズ

    # コンストラクタ
    def __init__(self, rect, offset0, offset1):
        strip = pygame.image.load("image/characters.png")

        # 画像用の小さな描画領域を作成する
        # pygame.SRCALPHAを指定すると、背景を透過することができる
        self.images = (
            pygame,
            surface((24, 24), pygame.SRCALPHA),
            pygame,
            surface((24, 24), pygame.SRCALPHA),
        )

    # 移動処理
    def move(self, diff_x, diff_y):
        self.count += 1
        self.rect.move_ip(diff_x, diff_y)

    # 描画処理
    def draw(self):
        pass


# 自機クラス
class Ship(Drawable):
    # コンストラクタ
    def __init__(self):
        super().__init__(Rect(300, 550, 24, 24), 192, 192)

    # 移動処理
    def move(self, diff_x, diff_y):
        pass


# 自機ショットクラス
class Shot(Drawable):
    def __init__(self):
        super().__init__(Rect(0, 0, 24, 24), 0, 24)
        # 初期状態では描画しない
        self.on_draw = False


# 敵ビームクラス
class Beam(Drawable):
    def __init__(self):
        super().__init__(Rect(0, 0, 24, 24), 48, 72)
        # 敵ビームが撃たれるタイミングをランダムで決定する
        self.fire_timing = randint(5, 220)
        # 初期状態では描画しない
        self.on_draw = False


# エイリアンクラス
class Alien(Drawable):
    def __init__(self, rect, offset, score):
        super().__init__(rect, offset, offset + 24)
        # 倒した時のスコアを設定
        self.score = score
