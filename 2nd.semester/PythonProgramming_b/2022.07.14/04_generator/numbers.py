# 複数数字クラス
class Numbers:
    
    # コンストラクタ（数値リストをもらう）
    def __init__(self, num_list):
        self.num_list = num_list
        self.i = 0

    # イテレータとして、ジェネレータを返却
    def __iter__(self):
        return self.generate_nums()

    # ジェネレータ関数
    def generate_nums(self):
        # リストの要素数だけ繰り返す

            # i を１増加

            # リストの要素とｉの積を返却
            pass
