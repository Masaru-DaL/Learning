# 演習１
# PitcherクラスとBatterクラスの両方を継承するクラス
# TwoWayPlayerクラスを作成してください。
#
# このクラスのコンストラクタでは名前を受け取り、
# 親クラスそれぞれの「名前の設定」メソッドを「名前を引数として」
# 実行してください。
from pitcher import Pitcher
from batter import Batter


# 二刀流選手クラス
class TwoWayPlayer(Pitcher, Batter):
    def __init__(self, name):
        self.set_p_name(name)
        self.set_b_name(name)
