# 演習２
from random import randint

# ジョーカーゲームクラス
# ※今回の演習では、こちらのクラスは修正する必要はありません

# １～１０の穴のどれかにジョーカーがいます
# ジョーカーのいる穴を選んだらゲームオーバーです。
# ゲームオーバー処理は呼び出した方で行います。
class JokerGame:

    # この穴のセット名を指定
    def set_name(self, name):
        self.name = name
        
    # ジョーカーの穴を「１～10」で設定する
    def set_joker(self):
        self.joker = randint(1, 10)

    # 数字を１つもらって、それがジョーカーの居る穴じゃなければセーフ（True）
    # ジョーカーの居る穴ならアウト（False）を戻り値として返す
    # メッセージも出力する
    def is_gameover(self, no):
        is_gameover = (no == self.joker)
        if is_gameover:
            print(f"{self.name}の{no}番の穴には………ジョーカーがいました！ 残念！！")
        else:
            print(f"{self.name}の{no}番の穴には………ジョーカーはいません！")
        return is_gameover
