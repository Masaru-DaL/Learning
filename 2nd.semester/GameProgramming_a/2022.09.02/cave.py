import sys
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_SPACE

# ウインドウサイズ
W_WIDTH = 800
W_HEIGHT = 600
# 1. ゲーム開始時の自機の位置
START_SHIP_X = 0
START_SHIP_Y = 250
# 2. 自機の上下方向の加速度
MY_SHIP_ACCELERATION = 2
# 10. 壁の横幅
WALL_WIDTH = 10

pygame.init()   # pygameの初期化処理

# pygame の繰り返し処理の指定
# set_repeat（delay、interval）
# delay:最初の繰り返しの前のミリ秒数
# interval:その後、繰り返されるミリ秒数
pygame.key.set_repeat(5, 5)
surface = pygame.display.set_mode((W_WIDTH, W_HEIGHT))  # 画面表示
clock = pygame.time.Clock()                             # clock

# 3. 自機の位置
my_ship_pos = [START_SHIP_X, START_SHIP_Y]

# メイン処理
def main():
    # 4. 自機の上下方向の速度
    my_ship_speed = 0

    # 自機画像の読込
    ship_image = pygame.image.load("image/ship.png")
    clash_image = pygame.image.load("image/clash.png")

    # 11. 壁の穴のリストを作成する
    holes = []
    # 壁(穴)の数は、画面横幅÷壁の横幅
    for x in range(W_WIDTH // WALL_WIDTH):
        # Rect -> 四角形
        holes.append(Rect(x * WALL_WIDTH, 20, WALL_WIDTH, 560))

    # ゲームのループ処理
    while True:
        # 5. スペースキー押下フラグ
        is_space_down = False

        # イベント処理
        for event in pygame.event.get():
            # 終了処理
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # 6. スペースキー押下で、フラグをTrueにする
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    is_space_down = True

        # 7. 上下方向の自機の速度計算
        if is_space_down:
            # 自機を上に加速
            my_ship_speed -= MY_SHIP_ACCELERATION
        else:
            # 自機を下に加速
            my_ship_speed += MY_SHIP_ACCELERATION

        # 8. 自機の位置を設定([1] -> y座標)
        my_ship_pos[1] += my_ship_speed

        # 12. 壁の描画
        surface.fill((0, 255, 0))
        # 13. 壁の穴の描画
        for hole in holes:
            pygame.draw.rect(surface, (0, 0, 0), hole)


        # 9. 自機の描画
        surface.blit(ship_image, my_ship_pos)

        # 画面の更新
        pygame.display.update()
        # クロック（時間間隔）の設定
        clock.tick(15)

if __name__ == '__main__':
    main()
