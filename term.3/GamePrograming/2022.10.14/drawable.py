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
        # Ｂ－１）画像用の小さな描画領域を作成する
        # Ｂ－２）pygame.SRCALPHAを指定すると、背景を透過することができる
        self.images = (
            pygame.Surface((24, 24), pygame.SRCALPHA),
            pygame.Surface((24, 24), pygame.SRCALPHA),
        )
        self.rect = rect  # Ｂ－３）描画用の四角
        self.count = 0  # Ｂ－４）描画用のカウンタ
        self.on_draw = True  # Ｂ－５）描画フラグ（Falseでは描画しない）
        # Ｂ－６）画像１
        self.images[0].blit(strip, (0, 0), Rect(offset0, 0, 24, 24))
        # Ｂ－７）画像２
        self.images[1].blit(strip, (0, 0), Rect(offset1, 0, 24, 24))

    # 移動処理
    def move(self, diff_x, diff_y):
        self.count += 1
        self.rect.move_ip(diff_x, diff_y)

    # 描画処理
    def draw(self):
        # Ｂ－８）描画フラグがFalseの場合は描画しない
        if self.on_draw:
            # Ｂ－９）countの値によって、描画する画像を入れ替える
            if self.count % 2 == 0:
                self.surface.blit(self.images[0], self.rect.topleft)
            else:
                self.surface.blit(self.images[1], self.rect.topleft)


# 自機クラス
class Ship(Drawable):
    # コンストラクタ
    def __init__(self):
        super().__init__(Rect(300, 550, 24, 24), 192, 192)

    # 移動処理
    def move(self, diff_x, diff_y):
        # Ｂ－１０）自機の移動、移動後の位置が画面外に行かない場合は移動する
        if 12 <= self.rect.centerx + diff_x < self.window_size[0] - 12:
            super().move(diff_x, diff_y)
        # Ｂ－１１mainへ）画面外に行ってしまう場合は移動距離を０にするが、移動処理は行う
        else:
            super().move(0, 0)


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
