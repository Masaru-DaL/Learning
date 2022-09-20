import random
import pygame
from pygame.locals import Rect

# エサクラス
# ※エサ全部で１つのインスタンスとして使用します
class Foods:

    # エサの色
    FOOD_COLOR = (0, 255, 0)

    # エサの画像
    food_image = pygame.image.load("114812.png")

    # 16. コンストラクタ
    def __init__(self):
        # エサを空のリストとして用意
        self.food_list = []

    # 17. 画面上のエサを配置
    def add(self, snake, column_count, row_count):
        # エサを配置できるまでずっと繰り返す
        while True:
            # エサの位置をランダムで決定する
            column_pos = random.randint(0, column_count-1)
            row_pos = random.randint(0, row_count-1)
            food_pos = (column_pos, row_pos)
            # エサの位置が、すでにエサの位置だったらやり直し
            if food_pos in self.food_list:
                continue
            # エサの位置が、ヘビの体のある位置ならやり直し
            if food_pos in snake.body:
                continue

            # エサを配置して、繰り返しを終了する
            self.food_list.append(food_pos)
            break

    # 23. 画面上のエサを別の場所に移動させる処理
    def move(self, snake, food_pos, column_count, row_count):
        # 画面上にエサを配置
        self.add(snake, column_count, row_count)
        # エサのリストのインデックス番号を取得
        food_list_index = self.food_list.index(food_pos)
        # そのエサをリストから取り除く
        del self.food_list[food_list_index]

    # 18. エサの描画処理
    def draw(self, surface, width, height):
        # エサの数だけ、丸を描画する
        for pos in self.food_list:
            surface.blit(Foods.food_image, (pos[0]*width, pos[1]*height))
            # pygame.draw.ellipse(surface, Foods.FOOD_COLOR,
            #                     Rect(pos[0]*width, pos[1]*height, width, height))
