import sys
import random
import pygame
from snake import Snake
from foods import Foods
from pygame.locals import QUIT, KEYDOWN, K_DOWN

BLOCK_ROWS = 20     # マスの縦の数
BLOCK_COLUMNS = 20     # マスの横の数
BLOCK_HEIGHT = 30   # マスの高さ
BLOCK_WIDTH = 30    # マスの幅
WINDOW_HEIGHT = BLOCK_ROWS * BLOCK_HEIGHT   # 画面の高さ
WINDOW_WIDTH = BLOCK_COLUMNS * BLOCK_WIDTH     # 画面の幅

FOOD_COUNT = 10                             # エサの数
LINE_COLOR = (64, 64, 64)                   # 区切り線の色
MSG_COLOR = (255, 0, 0)                     # メッセージの色

# Pygameの初期設定等
pygame.init()
surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
# フォント
msg_font = pygame.font.SysFont("Arial", 100)

# 1. 画面の描画処理
# 14. 引数にsnakeの追加
# 22. 引数にfoodsの追加
def paint(snake, foods, display_message, display_message_pos):
    # 2. 画面を黒で塗りつぶす処理
    surface.fill((152,251,152))

    # 15. ヘビの描画処理
    snake.draw(surface, BLOCK_WIDTH, BLOCK_HEIGHT)

    # 23. エサの描画処理
    foods.draw(surface, BLOCK_WIDTH, BLOCK_HEIGHT)

    # 3. 縦の線を引く
    for index in range(BLOCK_COLUMNS):
        pygame.draw.line(surface, LINE_COLOR,
                        # 始点の指定
                        (index * BLOCK_WIDTH, 0),
                        # 終点の指定
                        (index * BLOCK_WIDTH, WINDOW_HEIGHT))
    # 4. 横の線を引く
    for index in range(BLOCK_ROWS):
        pygame.draw.line(surface, LINE_COLOR,
                        (0, index * BLOCK_HEIGHT),
                        (WINDOW_WIDTH, index * BLOCK_HEIGHT))

    if display_message != "":
        msg = msg_font.render(display_message, True, MSG_COLOR)
        surface.blit(msg, display_message_pos)


    # 5. 画面を更新する
    pygame.display.update()

# メイン処理
def main():
    # ゲームオーバーフラグ
    is_gameover = False
    # 画面のメッセージと位置
    display_message = ""
    display_message_pos = (0, 0)

    # 初期状態は、下キーが押されているものとする
    key = K_DOWN

    # 10. ヘビの体の初期値の設定(体の長さが3(仮), 隣り合った位置にする)
    f_body = [(10, 10), (10, 9), (10, 8)]

    # 11. ヘビクラスのインスタンスを作成
    snake = Snake(f_body)

    # 19. エサクラスのインスタンスを作成
    foods = Foods()

    # 20. エサの数だけエサを配置する
    for food in range(FOOD_COUNT):
        foods.add(snake, BLOCK_COLUMNS, BLOCK_ROWS)

    # メイン繰り返し処理
    while True:
        # イベント取得
        for event in pygame.event.get():
            # 終了イベントの場合、ゲームを終了する
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # キーが押された場合、そのキーを保持する
            elif event.type == KEYDOWN:
                key = event.key

        # ゲームオーバーの場合、メッセージを設定する
        if is_gameover:
            display_message = "GAME OVER"
            display_message_pos = (85, 120)

        # ゲームオーバーでない場合
        else:
            # 12. ヘビの移動処理(キーを引数にする)
            is_gameover = snake.move(key, foods, BLOCK_ROWS, BLOCK_COLUMNS)

        # 6. 画面描画処理関数の実行
        # 13. paint()の引数にsnakeを指定する
        # 21. 引数にfoodsの追加
        paint(snake, foods, display_message, display_message_pos)
        clock.tick(5)

if __name__ == '__main__':
    main()
