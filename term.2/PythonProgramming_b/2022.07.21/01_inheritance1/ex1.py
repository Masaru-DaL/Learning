# 演習１
# まずはクラス Dragon を dragon.py に作成して下さい
# 内容は dragon.py に記載してあります。
#
# Dragonクラスのインスタンスを作成します、
# その後、任意の回数（５回程度）、以下の処理を繰り返して下さい
# ・ランダムで以下の処理のどちらかを行う（確率は任意）
#   インスタンスのattack()を実行する
#   インスタンスのbress()を実行する

from dragon import Dragon
from slime import Slime
import random

monster_dragon = Dragon()
monster_slime = Slime()
monster_slime.set_name("すらりん")

for i in range(10):
  random_num = random.randint(1, 100)
  if random_num < 10:
    monster_slime.attack()
  if random_num > 10 and random_num < 50:
    monster_dragon.attack()
  elif random_num > 50:
    monster_dragon.breathe()
