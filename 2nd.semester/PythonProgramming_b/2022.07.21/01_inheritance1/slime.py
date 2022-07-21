from asyncio import constants
from copyreg import constructor
from monster import Monster

# 新しくSlimeクラスを作成し、Monsterクラスを継承する
class Slime(Monster):

  def __init__(self):
    self.set_name("スライム")
