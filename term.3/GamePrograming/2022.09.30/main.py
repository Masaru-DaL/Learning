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

    # ===== パドルとの反射チェック =====

    # ===== 壁との反射チェック =====


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
                pass

        # 各種描画処理
        surface.fill((0, 0, 0))  # 背景を黒に

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
