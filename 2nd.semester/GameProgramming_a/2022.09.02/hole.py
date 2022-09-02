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
