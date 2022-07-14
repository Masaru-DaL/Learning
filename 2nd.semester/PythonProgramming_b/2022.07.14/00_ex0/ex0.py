# 演習０
# まずはクラス Match を match.py に作成して下さい
#
# その後、このクラスのインスタンスを４つ作成します。
# インスタンス作成時には、相手のチーム名を引数に渡します
#
# 作った４つのインスタンスそれぞれのrecord_score関数を実施し、
# 試合結果を登録します。引数は自チームの得点と相手チームの得点です
# ※すべての試合の結果を登録しないでも構いません
#
# 最後に作った４つのインスタンスすべての試合結果を
# result_outputで出力して下さい


from unittest import result
from match import Match

team1 = Match("かながわず")
team2 = Match("とうきょうず")
team3 = Match("ほっかいどーず")
team4 = Match("おきなわず")

team1.record_score(1, 3)
team2.record_score(2, 3)
team3.record_score(1, 3)
team4.record_score(1, 1)

team1.result_output()
team2.result_output()
team3.result_output()
team4.result_output()
