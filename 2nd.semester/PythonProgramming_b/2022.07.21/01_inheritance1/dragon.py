# 演習１
# 「Monster」クラスを継承したクラス「Dragon」を作成します
from monster import Monster
class Dragon(Monster):

# このクラスでは以下のメソッドを持ちます
# ・コンストラクタ：
#   親クラスのset_name関数を引数「ドラゴン」で実行し、
#   名前を設定する

  def __init__(self):
    self.set_name("ドラゴン")

# ・炎を吐く関数（bress）：
#   「ドラゴンは炎を吐いた！」と出力する。
#   ただし「ドラゴン」の部分にはインスタンス変数を使用する
  def breathe(self):
    print(self.name + "は炎を吐いた！")
