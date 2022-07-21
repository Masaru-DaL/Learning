# 演習０
# まずはクラス MakeChar を makechar.py に作成して下さい
# 内容は makechar.py に記載してあります。
#
# その後、MakeChar クラスのインスタンスを作成します
# （引数に文字列を指定します）
# そのインスタンスを対象として、forループで反復可能な値を取得し、
# その結果を出力して下さい。

from makechar import MakeChar

char1 = MakeChar("Tree")

for i in char1:
  print(i)
