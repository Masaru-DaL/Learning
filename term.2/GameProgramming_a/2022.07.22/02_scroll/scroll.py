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

    # 背景画像の読み込み
    bg_image = pygame.image.load("../image/bg.png")
    # キャラクター画像の読み込みと、リストへの追加
    chara_images = []
    chara_images.append(pygame.image.load("../image/chara0.png"))
    chara_images.append(pygame.image.load("../image/chara1.png"))

    # タイマー（カウンタ）
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

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                screen = pygame.display.set_mode((640, 320), pygame.FULLSCREEN)
                

        # タイマーを160で割った値を、背景画像のx方向の位置とする
        x = timer % 160

        # 同じ画像を５つコピー
        for i in range(5):
            # ５つの画像それぞれを、x座標を160ずつずらして表示
            screen.blit(bg_image, [i*160-x, 0])
        # ２種類のキャラクター画像を、timerごとに交互に表示
        # 画像の表示位置は、基本で左上が基準となります
        # （tkinterで anchor="nw"を指定した場合と同じ）
        screen.blit(chara_images[timer%2], [224, 160])

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
