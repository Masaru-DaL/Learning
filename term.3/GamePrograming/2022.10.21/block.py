import pygame
from math import sqrt
from random import randint
from game import Game

# ブロッククラス
class Block:

    # コンストラクタ
    def __init__(self):
        # ブロックの種類をブロックデータからランダムで取得（７種類）
        self.type = Game.BLOCK_DATA[randint(0, 6)]
        # ブロックの回転状態をランダムで取得（４パターン）
        self.turn = randint(0, 3)
        # ブロック種類と回転状態をブロックデータとする
        self.data = self.type[self.turn]
        # ブロックのサイズを、ブロックデータの平方根とする
        # （四角は２、棒は４、他は３となる）
        self.size = int(sqrt(len(self.data)))
        # 初期位置（横）を、端にならないようにランダムで設定
        self.xpos = randint(2, 10 - self.size)
        # 初期位置（縦）を、下の１ブロックだけ見えるように設定
        self.ypos = 1  # 後で変更する
        # 落下タイミングを、現在のカウンタ＋間隔値に設定
        pass

    # ブロックが壁や他のブロックと衝突するかチェック
    def is_overlapped(self, xpos, ypos, turn):
        # ブロックを引数の回転に合わせたものとする
        pass
        # 横縦ともに、ブロックのサイズだけチェックを行う

        # チェック対象がフィールド内の場合にチェックする
        # ※画面外から落ちてくるので、そこでのチェックを防ぐため

        # 該当位置に今のブロックのデータがあって、
        # フィールドにもブロックのデータがある場合は
        # 「衝突した」としてTrueを返す

        # １箇所も衝突しなかったら、Falseを返す
        return False

    # ブロックを一段下へ移動する
    # 落下しきった場合、列の消去処理（消去した段の数を返す)
    def one_drop(self):
        erased = 0  # 消去した列の数

        # 落下タイミングを超えた場合

        # １つ下の段に落ちた場合にブロックや壁と衝突する場合

        # 横縦ともに、ブロックのサイズだけ処理を行う

        # 対象がフィールド内の場合

        # 現在ブロックの対象の色を取得

        # 色が無色でない場合

        # フィールドの該当の色を、ブロックの色で設定する

        # 揃った列の消去

        # 次のブロックへ切り替える

        # 下にブロックがない場合

        # つぎの落下タイミングを計算して、ブロックの位置を１つ下に落とす

        # 消した列の数を戻り値にする
        return erased

    # ブロックを描画する
    def draw(self):
        # ブロックデータの数だけ繰り返す
        for index in range(len(self.data)):
            # ブロックのサイズをもとに、x, yの位置を算出
            xpos = index % self.size
            ypos = index // self.size
            # ブロックデータの該当位置の色を設定
            val = self.data[index]
            # フィールド内、かつ、色が無色でない場合
            if (
                0 <= ypos + self.ypos < Game.HEIGHT
                and 0 <= xpos + self.xpos < Game.WIDTH
                and val != 0
            ):
                # 座標を計算
                x_pos = 25 + (xpos + self.xpos) * 25
                y_pos = 25 + (ypos + self.ypos) * 25
                # 四角形を描画
                pygame.draw.rect(Game.surface, Game.COLORS[val], (x_pos, y_pos, 24, 24))

    # ブロックを移動する
    def move(block, next_x, next_y, next_t):
        # 指定方向・回転で移動可能な場合
        pass
        # ブロックの位置、回転を更新

        # ブロックデータを回転に合わせて更新

        # ※移動出来ない場合は特に処理をしない

    # 行が全て埋まった段を消す
    @classmethod
    def erase_line(cls):
        erased = 0  # 消した列数
        ypos = 20  # 縦方向の位置を壁でない一番下に設定する
        # 一番上まで繰り返す

        # all関数：すべてTrueならTrueになる
        # 数字をBooleanとして扱うと、0以外はTrueなので、
        # 下記のif文では、列に0がひとつもない場合にTrueになる

        # 消した列数を１加算

        # フィールドから該当の列を削除

        # フィールドの先頭に空の列を追加（左右は壁）

        # 消さなかった場合、１つ上の列をチェックする
        # ※消した場合は同じ列をもう一度チェックする

        # 消した列数を戻り値にする
        return erased

    # 次のブロックに切り替える
    @classmethod
    def go_next_block(cls):
        # 操作ブロックを「次のブロック」にする。（空の場合は新規作成）
        Game.now_block = Game.next_block if Game.next_block != None else Block()
        # 次のブロックを新規作成
        Game.next_block = Block()
