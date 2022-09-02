# 18.
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_SPACE

# 19.
class Hole:
  # 10. 壁の横幅
  WALL_WIDTH = 10

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
    # 穴を角度だけ移動する(move_ip(x, y))
    self.rect.move_ip(0, Hole.hole_angle)

  # 28. 穴を左へ移動
  def left_move(self):
    self.rect.move_ip(Hole.WALL_WIDTH * -1, 0)
