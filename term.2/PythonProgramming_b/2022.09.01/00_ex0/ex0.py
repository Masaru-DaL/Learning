# 演習０
# まずはクラス Satellite を satellite.py に作成して下さい
# 内容は satellite.py に記載してあります。
#
# その後、Satellite クラスのインスタンスを作成します
# （引数に名前を指定します）
# そのインスタンスの以下のメソッドを順に実行してください。
# （必要ならば引数を指定してください）
# 「母惑星の設定（set_mother）」
# 「情報表示（print_info）」
# ※できたら、もう１つインスタンスを作って同様の処理をしてください。
from satellite import Satellite

satellite_1 = Satellite("月")
satellite_1.set_mother("地球")
satellite_1.print_info()
