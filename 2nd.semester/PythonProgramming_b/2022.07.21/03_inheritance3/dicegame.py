from dice import Dice 

# ダイスゲームクラス
class DiceGame(Dice):
    # コンストラクタでサイコロの数をもらう
    def __init__(self, count):
        self.count = count
    
    # サイコロを振って、合計値を出力する
    def roll_and_result(self):
        self.roll()
        total = self.get_total()
        print(f"サイコロ{self.count}個の目の合計は{total}です。")
        
