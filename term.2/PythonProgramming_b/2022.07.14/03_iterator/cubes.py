# ３乗数字クラス
class Cubes:

    # コンストラクタ（数値リストをもらう）
    def __init__(self, num_list):
        self.num_list = num_list
        self.i = 0      # 要素インデックスの初期値は０

    # イテレータとして、ジェネレータを返却
    def __iter__(self):
        return self

    def __next__(self):
        # リストの要素数を超えたら、例外
        if self.i >= len(self.num_list):
            raise StopIteration()

        # 該当する要素の３乗の数を変数に入れる
        num = self.num_list[self.i] ** 3
        # 要素インデックスを１増加
        self.i += 1
        # ３乗の変数を返却
        return num
