from mammal import Mammal
from seaanimal import SeaAnimal

# イルカクラス
class Dolphin(SeaAnimal, Mammal):

    # Mammalクラスのshow_infoを使用したい場合、新しく関数を定義する
    def mammal_show_info(self):
        Mammal.show_info(self)
