# 演習２
# RainクラスとThunderクラスの両方を継承するクラス
# Thunderstorm（雷雨）クラスを作成してください。
#
# このクラスのコンストラクタでは、
# ２つの親クラスそれぞれのコンストラクタを実行してください。
from rain import Rain
from thunder import Thunder
# 雷雨クラス
class Thunderstorm(Rain, Thunder):
  def __init__(self):
    Rain.__init__(self)
    Thunder.__init__(self)
