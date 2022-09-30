import sys
import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT
from ball import Ball
from paddle import Paddle
from block import Block

# ウィンドウサイズとメッセージの中央位置の設定
WINDOW_SIZE = (600, 800)
MSG_CENTER = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2)

# ボールのスピード（３段階）
SPEED_START = 7
SPEED_NORMAL = 10
SPEED_UPPER = 15

# ボール反射チェック処理
def check_reflection():

    global block_list

    # ===== ブロックとの反射チェック =====
    # 反射チェック前のブロックリストの数
    prevlen = len(block_list)
    # それぞれのブロックとボールが接触しているかを判定
    # 「接触していない」ブロックで新しくリストを作る
    block_list = [x for x in block_list if not x.rect.colliderect(ball.rect)]
    # 反射チェック前と後で、ブロックリストの数が変わっている場合
    if len(block_list) != prevlen:
        # ボールの進行方向を「上下方向に反転」させる
        ball.dir *= -1

    # ===== パドルとの反射チェック =====
    # パドルとボールが接触しているかを判定(colliderect: 四角の面同士の判定を行う関数)
    if paddle.rect.colliderect(ball.rect):
        # 接触した場合、パドルのどの位置と接触したかによってボールの進行方向を決定する
        ball.dir = (
            90 + (paddle.rect.centerx - ball.rect.centerx) / paddle.rect.width * 80
        )
        # スタート時のボールの速度をゆっくりから通常に変更する
        if ball.speed == SPEED_START:
            ball.speed = SPEED_NORMAL

    # ===== 壁との反射チェック =====
    # ボールが横の壁と接触した場合
    if ball.rect.centerx < 0 or ball.rect.centerx > WINDOW_SIZE[0]:
        # ボールを左右方向に反転させる
        ball.dir = 180 - ball.dir

    # ボールが上の壁と接触した場合
    if ball.rect.centery < 0:
        # ボールを上下方向に反転させる
        ball.dir = -ball.dir
        ball.speed = SPEED_UPPER


# Pygameの初期処理
pygame.init()
pygame.key.set_repeat(5, 5)  # キー押下判定を 5ms 単位にする
surface = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption("*** ブロックくずし ***")

# 画面に表示する各オブジェクトの作成
block_list = []  # ブロックリスト
paddle = Paddle()  # パドル
ball = Ball(SPEED_START)  # ボール

# メイン処理
def main():
    is_gameover = False
    is_clear = False

    # 表示メッセージ
    myfont = pygame.font.SysFont(None, 80)
    msg_clear = myfont.render("Cleared!", True, (255, 255, 0))
    msg_gameover = myfont.render("Game Over!", True, (255, 255, 0))

    # ===== ブロックリストの作成処理 =====
    # ブロックの色リスト
    block_colors = [
        (255, 0, 0),
        (255, 165, 0),
        (242, 242, 0),
        (0, 128, 0),
        (128, 0, 128),
        (0, 0, 250),
    ]

    # ブロックの色リストの数だけ繰り返す
    for ypos, color in enumerate(block_colors, start=0):
        # 横は5つ並べる
        for xpos in range(0, 5):
            # x方向、y方向にちょうど良い感覚を開けて配置
            block_list.append(Block(color, xpos * 100 + 60, ypos * 50 + 40))

    # メイン処理ループ
    while True:
        # ボール反射チェック処理
        check_reflection()

        # ===== イベント処理 =====
        for event in pygame.event.get():
            # 終了処理
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # キー押下処理
            elif event.type == KEYDOWN:
                # 左右キーの場合、パドルを移動する(引数で方向を指定)
                if event.key == K_LEFT:
                    paddle.move(-1)
                elif event.key == K_RIGHT:
                    paddle.move(1)

        # ボールの移動処理
        if ball.rect.centery <= WINDOW_SIZE[1]:
            ball.move()
        # ボールが画面下に行ったらゲームオーバー
        if ball.rect.centery > WINDOW_SIZE[1]:
            is_gameover = True
        elif ball.rect.centery > WINDOW_SIZE[1]:
            is_gameover = True

        # 各種描画処理
        surface.fill((0, 0, 0))  # 背景を黒に
        paddle.draw(surface)  # パドルの描画
        ball.draw(surface)  # ボールの描画
        for block in block_list:
            block.draw(surface)  # ブロックの描画

        # クリア時のメッセージ表示
        if is_clear:
            # 表示位置の中心を調整
            msg_rect = msg_clear.get_rect()
            msg_rect.center = MSG_CENTER
            surface.blit(msg_clear, msg_rect.topleft)
        # ゲームオーバー時のメッセージ表示
        if is_gameover:
            # 表示位置の中心を調整
            msg_rect = msg_gameover.get_rect()
            msg_rect.center = MSG_CENTER
            surface.blit(msg_gameover, msg_rect.topleft)

        pygame.display.update()
        clock.tick(30)


if __name__ == "__main__":
    main()
