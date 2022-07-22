import pygame
import sys

def main():
    # Pygame の初期化処理：必ず書くと思って下さい
    pygame.init()
    # ウィンドウタイトルの設定
    pygame.display.set_caption("画像表示とスクロール")
    # ウィンドウサイズの指定
    screen = pygame.display.set_mode((640, 360))
    # フレームレート指定のためのオブジェクトの作成
    clock = pygame.time.Clock()

    # 線を描画(画面, (色RGB), (始点), (終点), 線の幅)
    pygame.draw.line(screen, (255, 255, 255), (50, 50), (200, 200), 3)
    pygame.draw.line(screen, (255, 0, 255), [20, 150], [250, 250], 3)

    # 四角形を描画(画面, (色RGB), 四角[始点x, 始点y, 幅, 高さ], 線の幅)
    pygame.draw.rect(screen, (255, 0, 0), [200, 100, 150, 50], 5)

    # 円を描画(画面, (色RGB), [中心点], 半径, 線の幅)
    pygame.draw.circle(screen, (0, 255, 255), [250, 250], 80, 3)

    import random
    x1 = 20
    y1 = 150
    x2 = 250
    y2 = 250
    d = [-5, -10, 0, 5, -10]

    # メインループ：Pygame ではこのループ内の処理が繰り返される
    while True:
        # タイマーを１増やす

        # ウィンドウの×ボタン等で終了するための処理
        # 大体こう書くと思って下さい
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()       # Pygameの終了
                sys.exit()          # プログラム自体の終了

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                screen = pygame.display.set_mode((640, 320), pygame.FULLSCREEN)



        # 画面の更新処理
        pygame.display.update()

        # フレームレートの指定
        # 下記の書き方だと、１秒間に５回処理が行われる
        # ※この記述を入れないと、コンピュータの処理を専有してしまい、
        # コンピュータが他の処理を余りできなくなってしまいます
        clock.tick(10)

# このプログラム自体が起動された場合のみ実施
# import された場合は動作しない
if __name__ == "__main__":
    main()
