# 18.
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_SPACE
# 34.
from random import randint
# # 32.
# from cave import W_HEIGHT

# 19.
class Hole:
  # 10. 壁の横幅
  WALL_WIDTH = 10

  # 32. 画面の横幅
  W_HEIGHT = 0

  # 35. 壁の角度の最大値
  ANGLE_MAX = 6

  # 37. 一段階ごとに穴が小さくなるサイズ
  NARROW_SIZE = 10

  # 38. 最小の穴のサイズ
  MIN_HOLE_SIZE = 100

  # 25. 穴のずれ角度
  hole_angle = 1

  # 42. レベル
  level = 1

  # 20. コンストラクタ
  def __init__(self, x):
    self.rect = Rect(x, 20, Hole.WALL_WIDTH, 560)

  # 26. 穴の設定
  def set_hole(self, top, height):
    self.rect.top = top
    self.rect.height = height

  # 39. 穴のサイズの算出
  def calc_hole_size(self):
    # 穴のサイズを計算
    self.hole_size = self.rect.height
    # 穴のサイズを小さくする
    self.hole_size -= Hole.NARROW_SIZE
    # 最小値を設定し、無限に小さくなるのを防ぐ
    if self.hole_size < Hole.MIN_HOLE_SIZE:
      self.hole_size = Hole.MIN_HOLE_SIZE

  # 27. 穴を角度分移動
  def move_angle(self):
    # 36. 穴をコピーして、一度動かしてみる
    check_rect = self.rect.copy()
    check_rect.move_ip(0, Hole.hole_angle)
    # 移動後の位置が、上の端に達していたら新しい角度(下向き)を設定する
    if check_rect.top <= 0:
      Hole.hole_angle = randint(1, Hole.ANGLE_MAX)

      # 40. 穴のサイズを算出する
      self.calc_hole_size()
      # 40. 穴のサイズを計算後の値にする
      self.rect.height = self.hole_size
      # 42. レベルを1増やす
      Hole.level += 1

    # 移動後の位置が、下の端に達していたら新しい角度(上向き)を設定する
    elif check_rect.bottom >= Hole.W_HEIGHT:
      Hole.hole_angle = randint(1, Hole.ANGLE_MAX) * -1

      # 41. 穴のサイズを算出する
      self.calc_hole_size()
      # 41. 穴の上端をずらして、穴のサイズを計算後の値にする
      self.rect.top -= Hole.hole_angle
      self.rect.height = self.hole_size
      # 42. レベルを1増やす
      Hole.level += 1

    # 穴を角度だけ移動する(move_ip(x, y))
    self.rect.move_ip(0, Hole.hole_angle)

  # 28. 穴を左へ移動
  def left_move(self):
    self.rect.move_ip(Hole.WALL_WIDTH * -1, 0)
