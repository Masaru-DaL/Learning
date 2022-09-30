import sys
from random import randint
import pygame
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_LEFT, K_RIGHT, K_UP, K_DOWN

# pygameの初期化処理
pygame.init()
surface = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
# ウィンドウにタイトルを表示
pygame.display.set_caption("*** SUTURN VOYGER ***")

# メイン処理
def main():
    # ゲームオーバーフラグ
    is_gameover = False
    # 画面表示用画像の読み込み
    scope_image = pygame.image.load("image/scope.png")
    rock_image = pygame.image.load("image/rock.png")
    
    # ゲームメインループ
    while True:
        # イベント取得
        for event in pygame.event.get():
            # 終了イベントの場合、アプリ終了
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # 背景を黒で描画
        surface.fill((0, 0, 0))
        # 宇宙船内部の描画
        surface.blit(scope_image, (0, 0))

        # 画面描画の更新
        pygame.display.update()
        # 一定のタイミングでループする
        clock.tick(20)

# メイン処理呼び出し
if __name__ == '__main__':
    main()
