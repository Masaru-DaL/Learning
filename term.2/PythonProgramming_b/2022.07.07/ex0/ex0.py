# 演習０
# まず、animal.pyに Animal クラスを作成して下さい。
# Animalクラスの内容はanimal.pyに書いてあります。
#
# 続いて、このプログラムファイルに以下の処理を書きます。
# １）Animalクラスをインポートする
# ２）Animakクラスのインスタンスを作る
#     作る際に、動物の種類と鳴き声を引数にする
# ３）作ったインスタンスのcrowingを実行する
#     引数に、鳴く回数を指定する
# ４）２）と３）を別の動物（別のインスタンス）で実行する


from animal import Animal


animal1 = Animal("ひよこ", "ぴよぴよ")
animal1.crowing(3)

animal2 = Animal("ぞうさん", "ぱおーん")
animal2.crowing(0)

animal3 = Animal("きりんさん", "きりんです")
animal3.crowing(4)
