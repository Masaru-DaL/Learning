# 演習０
# まずはクラス TwoWayPlayer を twoway.py に作成して下さい
# 内容は twoway.py に記載してあります。
#
# その後、TwoWayPlayer クラスのインスタンスを作成します
# （引数に名前を指定します）
# そのインスタンスの以下のメソッドを順に実行してください。
# （必要ならば引数を指定してください）
# 「set_era（防御率設定）」
# 「set_average（打率設定）」
# 「show_p_info（情報表示：投手）」
# 「show_b_info（情報表示：打者）」

from twoway import TwoWayPlayer

ootani = TwoWayPlayer("大谷")

ootani.set_era(2.00)
ootani.set_average(3.00)
ootani.show_p_info()
ootani.show_b_info()
