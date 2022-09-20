import sys
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_SPACE

# ウインドウサイズ
W_WIDTH = 800
W_HEIGHT = 600

pygame.init()   # pygameの初期化処理

# pygame の繰り返し処理の指定
# set_repeat（delay、interval）
# delay:最初の繰り返しの前のミリ秒数
# interval:その後、繰り返されるミリ秒数
pygame.key.set_repeat(5, 5)
surface = pygame.display.set_mode((W_WIDTH, W_HEIGHT))  # 画面表示
clock = pygame.time.Clock()                             # clock

# メイン処理
def main():

    # 自機画像の読込
    ship_image = pygame.image.load("image/ship.png")
    clash_image = pygame.image.load("image/clash.png")

    # ゲームのループ処理
    while True:

        # イベント処理
        for event in pygame.event.get():
            # 終了処理
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # 背景の描画
        surface.fill((0, 0, 0))

        # 自機の描画
        surface.blit(ship_image, (50, 100))

        # 画面の更新
        pygame.display.update()
        # クロック（時間間隔）の設定
        clock.tick(15)

if __name__ == '__main__':
    main()

