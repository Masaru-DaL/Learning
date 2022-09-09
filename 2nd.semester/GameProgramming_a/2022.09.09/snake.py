import pygame
import random
from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN, Rect

# ヘビクラス
class Snake:

    # ヘビの色
    SNAKE_COLOR1 = (0, 255, 255)
    SNAKE_COLOR2 = (129, 140, 42)
    SNAKE_COLOR3 = (38, 18, 1)
    SNAKE_COLOR4 = (166, 94, 31)
    SNAKE_COLOR = [SNAKE_COLOR1, SNAKE_COLOR2, SNAKE_COLOR3, SNAKE_COLOR4]
    RESULT_SNAKE_COLOR = random.choice(SNAKE_COLOR)


    # 7. コンストラクタ
    def __init__(self, body):
        # ヘビの体を表すインスタンス変数
        # 「(x, y)と位置を表すタプル」のリスト
        self.body = body


    # 8. ヘビ移動処理
    # 24. 引数の追加(foods, column_count, row_count)
    def move(self, key, foods, column_count, row_count):
        # ヘビの頭(先頭位置)を取得
        x, y = self.body[0]

        # 押されたキーに対応して、頭の位置を移動させる
        if key == K_LEFT:
            # 左キーが押されたら頭の位置をx座標-1する
            x -= 1
        elif key == K_RIGHT:
            x += 1
        elif key == K_UP:
            y -= 1
        elif key == K_DOWN:
            y += 1

        # 移動後の位置を新しい頭の位置にする
        # 頭が新しい場所に移動すると同時に末尾(ヘビのしっぽ)を削除する処理
        new_snake_head = (x, y)

        # ゲームオーバーフラグ
        is_gameover = False
        # ヘビの先頭が、ヘビの体と重なったらゲームオーバー
        if new_snake_head in self.body:
            is_gameover = True
        # ヘビの先頭が画面外に行ってしまったらゲームオーバー
        if not ((0 <= new_snake_head[0] < column_count) and (0 <= new_snake_head[1] < row_count)):
            is_gameover = True


        # ヘビの体に、新しい頭の位置を挿入する
        self.body.insert(0, new_snake_head)
        # ヘビの体の末尾を削除する
        #self.body.pop()
        # 25. ヘビの先頭が、エサの位置だったら
        if new_snake_head in foods.food_list:
            print("エサゲット！")
            foods.move(self, new_snake_head, column_count, row_count)

        # 26. エサの位置でない場合
        else:
            # ヘビの体の最後を削除する
            self.body.pop()

        return is_gameover

    # 9. ヘビの描画処理
    def draw(self, surface, width, height):
        # ヘビの体の数だけ、四角形を描画する
        for pos in self.body:
            pygame.draw.rect(surface, Snake.RESULT_SNAKE_COLOR,
                            Rect(pos[0]*width, pos[1]*height, width, height))
