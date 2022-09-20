# 演習２
# まずはクラス Thunderstorm を thunderstorm.py に作成して下さい
# 内容は thunderstorm.py に記載してあります。
#
# その後、Thunderstorm クラスのインスタンスを作成します
# そのインスタンスの以下のメソッドを実行してください。
# （必要ならば引数を指定してください）
# 「set_r_value（降水量設定）」「set_t_value（降水量設定）」※どちらが先でも可
# 「rain_info（情報表示：雨）」「thunder_info（情報表示：雷）」※どちらが先でも可
#
# このままだと、ちゃんと実行しても後から設定した値で上書きされてしまうと思います。
# 最後に、Rain または Thunder クラスのどちらかの
# インスタンス変数 value を他の名前に変えて、正しく動くようにしてください。
from thunderstorm import Thunderstorm

weather_1 = Thunderstorm()
weather_1.set_r_value(200)
weather_1.set_t_value(87)
weather_1.rain_info()
weather_1.thunder_info()
