import sys
import pygame
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_SPACE, K_LEFT, K_RIGHT, K_UP, K_DOWN
from random import randint
from math import radians, sin, cos
from drawable import Drawable, Rock, Shot, Ship

WINDOW_WIDTH = 800  # 画面の幅
WINDOW_HEIGHT = 800  # 画面の高さ
# ウィンドウサイズ
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
ROCK_COUNT = 4  # 画面上の初期の岩の数
START_ROCK_SIZE = 64  # 初期の岩のサイズ
START_ROCK_SPEED = 2  # 初期の岩の速さ
MAX_ROCK_LEVEL = 3  # 岩レベルの最大（３段階まで破壊される）
MAX_SHOT = 7  # 画面上に出る自機のショットの最大数
SHOT_SPEED = 10  # 自機のショットの速さ
SHOT_MAX_DISTANCE = 40  # 自機のショットの最大到達距離

# Pygame 初期化処理
pygame.init()
pygame.key.set_repeat(5, 5)
surface = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption("*** アステロイド ***")

# Drawableクラスのクラス変数に、画面の情報を表示する
Drawable.set_window_info(surface, WINDOW_SIZE)


# ============ キーイベント処理 ============
def key_event_handler(keymap, ship):
    # イベント処理ループ
    for event in pygame.event.get():
        # 終了処理
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if not event.key in keymap:
                keymap.append(event.key)

        elif event.type == KEYUP:
            keymap.remove(event.key)

    # 左右キーで自機を回転させる
    if K_LEFT in keymap:
        ship.theta += 5
    if K_RIGHT in keymap:
        ship.theta -= 5


# ============ メイン処理 ============
def main():
    # メッセージ表示用のフォント等
    sysfont = pygame.font.SysFont(None, 72)
    scorefont = pygame.font.SysFont(None, 36)
    msg_clear = sysfont.render("CLEAR!!", True, (0, 255, 225))
    msg_over = sysfont.render("GAME OVER!!", True, (0, 255, 225))

    keymap = []  # 押下キーのリスト
    shots = []  # ショットのリスト
    rocks = []  # 隕石のリスト
    is_gameover = False  # ゲームオーバーフラグ
    score = 0  # スコア
    back_x, back_y = 0, 0  # 描画用に背景をずらす量
    # 背景画像を読み込み(1600x1600)
    back_image = pygame.image.load("image/bg.png")

    # 自機クラスのインスタンスを作成
    ship = Ship()

    # 隕石クラスのインスタンスを、初期の隕石数だけ作成
    while len(rocks) < ROCK_COUNT:
        # 隕石の位置を画面上のランダムで作成
        pos = randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)
        # 隕石クラスのインスタンスを作成
        rock = Rock(1, pos, START_ROCK_SIZE, START_ROCK_SPEED)
        # 隕石をリストに追加
        rocks.append(rock)

    # メインループ
    while True:
        # キーイベント処理の関数を実行
        key_event_handler(keymap, ship)

        # ゲームオーバーでない場合
        if not is_gameover:
            pass

        # 描画処理
        surface.fill((0, 0, 0))

        # 隕石の描画
        for rock in rocks:
            rock.draw()

        # メッセージの描画
        if is_gameover:
            if len(rocks) == 0:
                msg_rect = msg_clear.get_rect()
                msg_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
                surface.blit(msg_clear, msg_rect.topleft)
            else:
                msg_rect = msg_over.get_rect()
                msg_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
                surface.blit(msg_over, msg_rect.topleft)

        # 画面更新処理
        pygame.display.update()
        # 一定時間で処理を行う
        clock.tick(20)


# メイン処理を呼び出す
if __name__ == "__main__":
    main()
