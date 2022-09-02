# 18.
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_SPACE
# 34.
from random import randint
# 32.
from cave import W_HEIGHT

# 19.
class Hole:
  # 10. 壁の横幅
  WALL_WIDTH = 10

  # 32. 画面の横幅
  W_HEIGHT = 0

  # 35. 壁の角度の最大値
  ANGLE_MAX = 6

  # 25. 穴のずれ角度
  hole_angle = 1

  # 20. コンストラクタ
  def __init__(self, x):
    self.rect = Rect(x, 20, Hole.WALL_WIDTH, 560)

  # 26. 穴の設定
  def set_hole(self, top, height):
    self.rect.top = top
    self.rect.height = height

  # 27. 穴を角度分移動
  def move_angle(self):
    # 36. 穴をコピーして、一度動かしてみる
    check_rect = self.rect.copy()
    check_rect.move_ip(0, Hole.hole_angle)
    # 移動後の位置が、上の端に達していたら新しい角度(下向き)を設定する
    if check_rect.top <= 0:
      Hole.hole_angle = randint(1, Hole.ANGLE_MAX)
    # 移動後の位置が、下の端に達していたら新しい角度(上向き)を設定する
    elif check_rect.bottom >= Hole.W_HEIGHT:
      Hole.hole_angle = randint(1, Hole.ANGLE_MAX) * -1

    # 穴を角度だけ移動する(move_ip(x, y))
    self.rect.move_ip(0, Hole.hole_angle)

  # 28. 穴を左へ移動
  def left_move(self):
    self.rect.move_ip(Hole.WALL_WIDTH * -1, 0)
