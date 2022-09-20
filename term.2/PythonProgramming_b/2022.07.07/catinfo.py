from cat import Cat

c1 = Cat("たま", "化け猫")
c1.output_info()

# 関数から戻り値として返ってきた名前を指定する
c1_n = c1.get_name()
print(f"インスタンスc1の名前は{c1_n}です。")

# c2で指定したnameを直接指定する
c2 = Cat("くろ", "黒猫")
print(f"インスタンスc2の名前は{c2.name}です。")

c2.name = "しろたま"
c2.favorite = "ひと"
c2.output_info()
