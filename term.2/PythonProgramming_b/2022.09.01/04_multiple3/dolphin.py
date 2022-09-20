from mammal import Mammal
from seaanimal import SeaAnimal

# イルカクラス
class Dolphin(Mammal, SeaAnimal):

    # コンストラクタ
    def __init__(self):
        Mammal.__init__(self)
        SeaAnimal.__init__(self)
