import pygame
from pygame.locals import Rect
from math import radians, sin, cos
from random import randint

# ============ 描画クラス ============
class Drawable:

    game_surface = None  # ゲームで描画する対象
    game_window_size = None  # ゲームウィンドウのサイズ

    # クラスメソッド：ウィンドウ情報の設定
    @classmethod
    def set_window_info(cls, surface, window_size):
        cls.game_surface = surface  # 描画対象の画面
        cls.game_window_size = window_size  # 描画対象の画面のサイズ

    # コンストラクタ
    def __init__(self, rect):
        self.rect = rect  # 描画する四角
        self.step = [0, 0]  # 移動する量

    # 移動処理
    def move(self):
        # 移動対象の中心を取得
        rect = self.rect.center
        # 描画対象を「移動する量」だけ移動する
        # その後、画面サイズで割ったあまりにすることで、画面端に行った場合に反対側から出現する
        xpos = (rect[0] + self.step[0]) % Drawable.game_window_size[0]


# ============ 隕石クラス ============
class Rock(Drawable):
    def __init__(self, level, pos, size, speed):
        super().__init__(Rect(0, 0, size, size))
        self.image = pygame.image.load("image/rock.png")
        self.rect.center = pos  # 隕石の中央位置を設定する

    # 描画処理
    def draw(self):
        # 隕石を描画
        Rock.game_surface.blit(self.image, self.rect)

    # １ループ当たりの処理
    def tick(self):
        pass


# ============ 自機クラス ============
class Ship(Drawable):
    def __init__(self):
        super().__init__(Rect(355, 370, 90, 60))
        self.image = pygame.image.load("image/ship.png")
        self.bang = pygame.image.load("image/bang.png")
        self.theta = 0  # Ｃ－１）自機の向き

    # 描画処理
    def draw(self):
        # Ｃ－２）自機の角度に合わせて画像を回転させる
        rotated = pygame.transform.rotate(self.image, self.theta)
        # Ｃ－３）回転させた画像から四角を得て、その中心を自機の中心に合わせる
        rect = rotated.get_rect()
        rect.center = self.rect.center
        # Ｃ－４mainへ）回転させた画像と、上記で設定した四角をもとに、画像を表示する
        Ship.game_surface.blit(rotated, rect)

    # １ループ当たりの処理
    def tick(self):
        pass


# ============ ショットクラス ============
class Shot(Drawable):

    pass
