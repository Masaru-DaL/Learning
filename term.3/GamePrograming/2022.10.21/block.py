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
        self.ypos = 1 - self.size
        # 落下タイミングを、現在のカウンタ＋間隔値に設定
        self.drop_timing = Game.count + Game.interval

    # ブロックが壁や他のブロックと衝突するかチェック
    def is_overlapped(self, xpos, ypos, turn):
        # ブロックを引数の回転に合わせたものとする
        data = self.type[turn]
        # 横縦ともに、ブロックのサイズだけチェックを行う
        for y_offset in range(self.size):
            for x_offset in range(self.size):
                # チェック対象がフィールド内の場合にチェックする
                # ※画面外から落ちてくるので、そこでのチェックを防ぐため
                if (
                    0 <= xpos + x_offset < Game.WIDTH
                    and 0 <= ypos + y_offset < Game.HEIGHT
                ):

                    # 該当位置に今のブロックのデータがあって、
                    # フィールドにもブロックのデータがある場合は
                    # 「衝突した」としてTrueを返す
                    if (
                        data[y_offset * self.size + x_offset] != 0
                        and Game.field[ypos + y_offset][xpos + x_offset] != 0
                    ):
                        return True
        # １箇所も衝突しなかったら、Falseを返す
        return False

    # ブロックを一段下へ移動する
    # 落下しきった場合、列の消去処理（消去した段の数を返す)
    def one_drop(self):
        erased = 0  # 消去した列の数

        # 落下タイミングを超えた場合
        if self.drop_timing < Game.count:
            # １つ下の段に落ちた場合にブロックや壁と衝突する場合
            if self.is_overlapped(self.xpos, self.ypos + 1, self.turn):
                # 横縦ともに、ブロックのサイズだけ処理を行う
                for y_offset in range(self.size):
                    for x_offset in range(self.size):
                        # 対象がフィールド内の場合
                        if (
                            0 <= self.xpos + x_offset < Game.WIDTH
                            and 0 <= self.ypos + y_offset < Game.HEIGHT
                        ):
                            # 現在ブロックの対象の色を取得
                            val = self.data[y_offset * self.size + x_offset]
                            # 色が無色でない場合
                            if val != 0:
                                # フィールドの該当の色を、ブロックの色で設定する
                                Game.field[self.ypos + y_offset][
                                    self.xpos + x_offset
                                ] = val
                # 揃った列の消去
                erased = Block.erase_line()
                # 次のブロックへ切り替える
                Block.go_next_block()
            # 下にブロックがない場合
            else:
                # つぎの落下タイミングを計算して、ブロックの位置を１つ下に落とす
                self.drop_timing = Game.count + Game.interval
                self.ypos += 1
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
        if not block.is_overlapped(next_x, next_y, next_t):
            # ブロックの位置、回転を更新
            block.xpos = next_x
            block.ypos = next_y
            block.turn = next_t
            # ブロックデータを回転に合わせて更新
            block.data = block.type[block.turn]
        # ※移動出来ない場合は特に処理をしない

    # 行が全て埋まった段を消す
    @classmethod
    def erase_line(cls):
        erased = 0  # 消した列数
        ypos = 20  # 縦方向の位置を壁でない一番下に設定する
        # 一番上まで繰り返す
        while ypos >= 0:
            # all関数：すべてTrueならTrueになる
            # 数字をBooleanとして扱うと、0以外はTrueなので、
            # 下記のif文では、列に0がひとつもない場合にTrueになる
            if all(Game.field[ypos]):
                # 消した列数を１加算
                erased += 1

                # フィールドから該当の列を削除
                del Game.field[ypos]
                # フィールドの先頭に空の列を追加（左右は壁）
                Game.field.insert(0, [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8])
            # 消さなかった場合、１つ上の列をチェックする
            # ※消した場合は同じ列をもう一度チェックする
            else:
                return ypos

        # 消した列数を戻り値にする
        return erased

    # 次のブロックに切り替える
    @classmethod
    def go_next_block(cls):
        # 操作ブロックを「次のブロック」にする。（空の場合は新規作成）
        Game.now_block = Game.next_block if Game.next_block != None else Block()
        # 次のブロックを新規作成
        Game.next_block = Block()
