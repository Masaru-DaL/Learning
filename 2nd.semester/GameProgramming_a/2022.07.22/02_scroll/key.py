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

    C_WHITE = (255, 255, 255)
    C_RED = (255, 0, 0)

    font = pygame.font.Font(None, 60)

    timer = 0


    # メインループ：Pygame ではこのループ内の処理が繰り返される
    while True:
        # タイマーを１増やす
        timer += 1


        # ウィンドウの×ボタン等で終了するための処理
        # 大体こう書くと思って下さい
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()       # Pygameの終了
                sys.exit()          # プログラム自体の終了

        screen.fill((0, 0, 0))

        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            t1 = font.render("Up", True, C_RED, C_WHITE)
            screen.blit(t1, [150, 50])

        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN]:
            t1 = font.render("Down", True, C_RED, C_WHITE)
            screen.blit(t1, [150, 150])

        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            t1 = font.render("Right", True, C_RED, C_WHITE)
            screen.blit(t1, [250, 100])

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            t1 = font.render("Left", True, C_RED, C_WHITE)
            screen.blit(t1, [50, 100])

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
