from dolphin import Dolphin

dolphin_1 = Dolphin()
dolphin_1.set_name("いるか君")

# show_infoは親クラスのMammal, SeaAnimalの両方にある。
dolphin_1.show_info()
# 出力結果 -> いるか君は海の中で生活します
# class Dolphin(SeaAnimal, Mammal): ここで先に指定したSeaAnimalのshow_infoが使用される。

# 新しくDolphinクラスに定義した関数を呼び出す
dolphin_1.mammal_show_info()
