# 演習０
# クラス「MakeChar」を作成します
#
# このクラスでは以下のメソッドを持ちます

class MakeChar:

# ・コンストラクタ：
#   引数として文字列を１つもらい、インスタンス変数chに入れる
#   インスタンス変数のループカウンタ i の初期値を0にする
    def __init__(self, ch):
        self.ch = ch
        self.i = 0

# ・イテレータ関数：
#   ジェネレータ関数を実行した結果を返す
    def __iter__(self):
        return self.generate_nums()

# ・ジェネレータ関数（任意の名前）：
#   インスタンス変数chの文字列の文字だけ以下の処理を繰り返す
#   インスタンス変数iを1増やす
#   ch を i 個繋げた文字列を、ジェネレータとして返却する(yield)
    def generate_nums(self):
        # self.chの各文字に対して繰り返し
        for c in self.ch:
            self.i += 1
            yield c * self.i
