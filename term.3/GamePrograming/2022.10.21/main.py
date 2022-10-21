import sys
import pygame
from pygame.locals import (
    QUIT,
    KEYDOWN,
    K_LEFT,
    K_RIGHT,
    K_DOWN,
    K_UP,
    K_SPACE,
    K_RETURN,
)
from block import Block
from game import Game

# Pythonの基本処理
pygame.init()
pygame.key.set_repeat(250, 30)
Game.surface = pygame.display.set_mode([600, 600])
clock = pygame.time.Clock()
pygame.display.set_caption("*** 落ち物パズル ***")

# ゲーム情報初期化処理
def init_game_info():
    # 各クラス変数に初期値を設定する
    Game.field = None
    Game.now_block = None
    Game.next_block = None
    Game.interval = 40
    Game.count = 0
    Game.score = 0
    Game.is_gameover = False
    # 次のブロックとの入れ替え処理を最初に１度実施
    Block.go_next_block()
    # すべて「０（黒）」でフィールドを作成
    Game.field = [[0 for _ in range(Game.WIDTH)] for _ in range(Game.HEIGHT)]
    # フィールドの左右の端を８（壁）にする
    for ypos in range(Game.HEIGHT):
        for xpos in range(Game.WIDTH):
            Game.field[ypos][xpos] = 8 if xpos == 0 or xpos == Game.WIDTH - 1 else 0

    # フィールドの一番下を８（壁）にする
    for index in range(Game.WIDTH):
        Game.field[Game.HEIGHT - 1][index]


# メイン処理
def main():
    smallfont = pygame.font.SysFont(None, 36)  # 小さい文字用のフォント
    largefont = pygame.font.SysFont(None, 72)  # 大きい文字用のフォント
    # ゲームオーバー用のメッセージ
    message_over = largefont.render("GAME OVER!!", True, (0, 255, 225))
    message_rect = message_over.get_rect()
    message_rect.center = (300, 300)

    # ゲーム情報の初期化処理を実行
    init_game_info()

    # ゲームのメインループ
    while True:
        key = None  # 入力値を初期化
        # イベント処理ループ
        for event in pygame.event.get():
            # 終了処理
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # キーが押されている場合、そのキーを保持する
            elif event.type == KEYDOWN:
                key = event.key

        # ゲームオーバーでない場合
        if not Game.is_gameover:
            # ゲームカウントを５加算
            Game.count += 5
            # ゲームカウントが1000の倍数になった場合
            if Game.count % 1000 == 0:
                # ゲームスピードの間隔を２減らす（最低１）
                Game.interval = max(1, Game.interval - 2)

            # ブロックの落下処理
            pass
            # 『２の「消去した列数」乗』かける100点のスコアを加算
            pass

            # 現在の位置と回転を「次の状態の位置と回転」に設定
            pass

            # キーイベント処理に応じて、次の状態を設定
            # スペースキーまたは上キーが押されている場合、１段階回転（３の次は０に）
            pass

            # 左右下キーはそれぞれの方向に移動
            pass

            # ブロックの移動を実施
            # ※回転や移動ができるかのチェックも行う
            pass

        # ゲームオーバーチェック
        # ゲームオーバーの場合、フラグがTrueになる
        Game.check_gameover()

        # ========== 描画処理 ==========
        Game.surface.fill((0, 0, 0))  # フィールドを黒で塗りつぶす
        # フィールドの値に応じて、四角形を描画
        for ypos in range(Game.HEIGHT):
            for xpos in range(Game.WIDTH):
                val = Game.field[ypos][xpos]
                pygame.draw.rect(
                    Game.surface,
                    Game.COLORS[val],
                    (25 + xpos * 25, 25 + ypos * 25, 24, 24),
                )

        # ゲームオーバーでない場合、操作中ブロックを描画
        if not Game.is_gameover:
            Game.now_block.draw()

        # 次のブロックの描画
        for ypos in range(Game.next_block.size):
            for xpos in range(Game.next_block.size):
                val = Game.next_block.data[xpos + ypos * Game.next_block.size]
                pygame.draw.rect(
                    Game.surface,
                    Game.COLORS[val],
                    (xpos * 25 + 460, ypos * 25 + 100, 24, 24),
                )

        # スコアの描画
        score_str = str(Game.score).zfill(6)
        score_image = smallfont.render(score_str, True, (0, 255, 0))
        Game.surface.blit(score_image, (500, 30))
        # ゲームオーバーの場合
        if Game.is_gameover:
            # メッセージを描画
            Game.surface.blit(message_over, message_rect)
            # エンターキーで、ゲーム情報を初期化して再プレイ可能
            if key == K_RETURN:
                init_game_info()

        pygame.display.update()  # 描画更新処理
        clock.tick(15)  # 一定時間処理


# メイン処理の呼び出し
if __name__ == "__main__":
    main()
