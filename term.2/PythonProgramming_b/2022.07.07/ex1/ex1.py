# 演習１
# 演習０の animal.py をこのフォルダ（ex1）にコピーして下さい。
#
# １）
# ３種類の動物のインスタンスを作成して下さい。
# その後、それらの動物の種類と鳴き方の説明を
# 「（種類）は（鳴き方）と鳴きます）」と出力して下さい。
# ※インスタンス変数を直接参照してOKです
#
# ２）
# インスタンス変数を直接変更する方法で、
# すべての動物の鳴き方を変更して下さい。
# その後、それぞれの動物のインスタンスに対して
# 回数を指定してcrowing を実行してください。
#
from animal import Animal

animal1 = Animal("ひよこ", "ぴよぴよ")
print(f"{animal1.kind}は{animal1.bark}と鳴きます\n")

animal2 = Animal("ぞうさん", "ぱおーん")
print(f"{animal2.kind}は{animal2.bark}と鳴きます\n")

animal3 = Animal("きりんさん", "きりんです")
print(f"{animal3.kind}は{animal3.bark}と鳴きます\n")

animal1.bark = "ひよひよ"
animal2.bark = "はおはお"
animal3.bark = "むきむき"

animal1.crowing(3)
animal2.crowing(3)
animal3.crowing(0)
