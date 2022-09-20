import random

# サイコロクラス
class Dice:
    # コンストラクタでサイコロの数をもらう
    def __init__(self, num):
        self.num = num
        self.faces = []
    
    # サイコロをnum個振って、その合計の目を保持する
    def roll(self):
        self.faces = []
        for i in range(self.num):
            d = random.randint(1, 6)
            self.faces.append(d)

    # サイコロの目をすべて足した値を返す
    def get_total(self):
        total = 0
        for d in self.faces:
            total += d
        return total
