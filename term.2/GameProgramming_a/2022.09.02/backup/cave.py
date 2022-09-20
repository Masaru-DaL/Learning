import sys
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_SPACE
# 21. Holeクラスのインポート
from hole import Hole

# ウインドウサイズ
W_WIDTH = 800
W_HEIGHT = 600

# 33. Holeクラスのクラス変数に、ウィンドウの縦幅を設定
Hole.W_HEIGHT = W_HEIGHT

# 1. ゲーム開始時の自機の位置
START_SHIP_X = 0
START_SHIP_Y = 250
# 2. 自機の上下方向の加速度
MY_SHIP_ACCELERATION = 2
# # 10. 壁の横幅
# WALL_WIDTH = 10

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
    # 14. ゲームオーバーフラグ
    is_gameover = False
    # 43. スコア
    score = 0

    # 44. フォントを指定
    game_font = pygame.font.SysFont("Arial", 32)

    # 自機画像の読込
    ship_image = pygame.image.load("image/ship.png")
    clash_image = pygame.image.load("image/clash.png")

    # 11. 壁の穴のリストを作成する
    holes = []
    # 壁(穴)の数は、画面横幅÷壁の横幅
    for x in range(W_WIDTH // Hole.WALL_WIDTH):
        # # Rect -> 四角形
        # holes.append(Rect(x * WALL_WIDTH, 20, WALL_WIDTH, 560))

        # 22. Holeクラスのインスタンスを作成する
        holes.append(Hole(x * Hole.WALL_WIDTH))

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

        # 15. ゲームプレイ中のみ以下の処理を行う
        if not is_gameover:
            # 7. 上下方向の自機の速度計算
            if is_space_down:
                # 自機を上に加速
                my_ship_speed -= MY_SHIP_ACCELERATION
            else:
                # 自機を下に加速
                my_ship_speed += MY_SHIP_ACCELERATION

            # 8. 自機の位置を設定([1] -> y座標)
            my_ship_pos[1] += my_ship_speed

            # 29. 新しい穴を生成する
            # 位置は一番右の穴の、1つ右にする
            right_rect = holes[-1].rect
            new_hole = Hole(right_rect.x + Hole.WALL_WIDTH)
            # 新しい穴の位置とサイズを、一番右の穴と同じにする
            new_hole.set_hole(right_rect.top, right_rect.height)
            # 新しい穴を、角度分ずらす
            new_hole.move_angle()

            # 30. 先頭の穴を削除して、新しい穴を追加する
            del holes[0]
            holes.append(new_hole)

            # 31. 全ての穴を左に1つ分ずらす
            for hole in holes:
                hole.left_move()

            # 16. 壁にぶつかったか判定する(my_ship_pos[1] + 60は自機の高さ分を調整する)
            # 「穴の上端より自機が上に行った場合」　または、
            # 「穴の下端より自機の下端が下に行った場合」　にぶつかったとする
            # if holes[0].top > my_ship_pos[1] or holes[0].bottom < my_ship_pos[1] + 60:

            # 23. Holeクラスの四角形を使用する
            if holes[0].rect.top > my_ship_pos[1] or holes[0].rect.bottom < my_ship_pos[1] + 60:
                is_gameover = True

        # 12. 壁の描画
        surface.fill((0, 255, 0))
        # 13. 壁の穴の描画
        for hole in holes:
            # pygame.draw.rect(surface, (0, 0, 0), hole)

            # 24. クラスからrectを取得して描画
            pygame.draw.rect(surface, (0, 0, 0), hole.rect)

        # 9. 自機の描画
        surface.blit(ship_image, my_ship_pos)

        # 45. レベルとスコアの表示
        level_info = game_font.render(f"Level: {Hole.level:3}", True,(0, 0, 255))
        score_info = game_font.render(f"Score: {score:6}", True,(0, 0, 255))
        surface.blit(level_info, (480, 20))
        surface.blit(score_info, (620, 20))

        # 17. ゲームオーバーの場合は爆発画像を上から描画する(爆発画像の方が大きいので調整)
        if is_gameover:
            surface.blit(clash_image, (my_ship_pos[0]-15, my_ship_pos[1]-30))
        # 46. ゲームオーバーでない場合、スコアを加算
        else:
            score += 1

        # 画面の更新
        pygame.display.update()
        # クロック（時間間隔）の設定
        clock.tick(15)

if __name__ == '__main__':
    main()
