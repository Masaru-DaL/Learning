import sys
from random import randint
import pygame
from pygame.locals import Rect, QUIT, KEYUP, KEYDOWN, K_LEFT, K_RIGHT, K_SPACE
from drawable import Drawable, Ship, Beam, Shot, Alien

WINDOW_WIDTH = 600  # 画面の幅
WINDOW_HEIGHT = 600  # 画面の高さ
# ウィンドウサイズ
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_WIDTH)

# Pygameの初期化処理
pygame.init()
pygame.key.set_repeat(5, 5)
surface = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption("*** インベーダー ***")

# Drawableクラスのクラス変数に、ゲームの画面情報を設定する
Drawable.set_window_info(surface, WINDOW_SIZE)

# ======= メイン処理 =======
def main():
    # フォント、メッセージ
    sysfont = pygame.font.SysFont(None, 72)
    scorefont = pygame.font.SysFont(None, 36)
    msg_clear = sysfont.render("CLEAR!!", True, (0, 255, 225))
    msg_over = sysfont.render("GAME OVER!!", True, (0, 255, 225))

    keymap = []  # キーマップ
    is_gameover = False  # ゲームオーバーフラグ
    is_left_move = True  # 左移動フラグ
    is_down_move = False  # 下移動フラグ
    move_interval = 20  # Ｃ－１）エイリアンの移動間隔
    loop_count = 0  # Ｃ－２）ループカウンタ
    score = 0  # スコア
    aliens = []  # インベーダーのリスト
    beams = []  # ビームのリスト
    ship = Ship()  # 自機のインスタンス
    shot = Shot()  # 自機ショットのインスタンス

    # Ｃ－３）エイリアンの初期配置
    # Ｃ－４）縦に配置するエイリアンの数だけ繰り返し
    for ypos in range(4):
        # Ｃ－５）上２列、下２列で、エイリアンの画像を変える
        # Ｃ－６）三項演算子での表現
        # Ｃ－７）ypos < 2 なら 96 、そうでないなら 144
        offset = 96 if ypos < 2 else 144
        # Ｃ－８）横に配置するエイリアンの数だけ繰り返し
        for xpos in range(10):
            # Ｃ－９）位置とサイズを計算して設定
            rect = Rect(100 + xpos * 50, ypos * 50 + 50, 24, 24)
            # Ｃ－１０）位置、画像位置、スコアを引数としてインスタンスを作成
            alien = Alien(rect, offset, (4 - ypos) * 10)
            # Ｃ－１１）エイリアンリストに追加
            aliens.append(alien)

    # ======= メイン処理 =======
    while True:
        ship_move_x = 0  # 自機の移動距離

        # イベント処理
        for event in pygame.event.get():
            # 終了処理
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # キーダウン処理
            elif event.type == KEYDOWN:
                if not event.key in keymap:
                    keymap.append(event.key)
            # キーアップ処理
            elif event.type == KEYUP:
                keymap.remove(event.key)

        # 左右キーの場合、自機の移動距離を設定
        if K_LEFT in keymap:
            ship_move_x = -5
        if K_RIGHT in keymap:
            ship_move_x = +5
        # スペースキーが押されて、自機ショットが発射されていない場合
        if K_SPACE in keymap and not shot.on_draw:
            # 自機ショットの位置を、自機の位置にする
            shot.rect.center = ship.rect.center
            # 自機ショットの描画フラグをTrueにする
            shot.on_draw = True

        # ゲームオーバーでない場合
        if not is_gameover:
            # Ｃ－１２）ループカウンタを１増やす
            loop_count += 1
            # 自機を移動する
            ship.move(ship_move_x, 0)
            # 自機ショットを移動する
            shot.move(0, -15)
            # 自機ショットが画面外に行った場合
            if shot.rect.bottom < 0:
                # 描画フラグをFalseにする
                shot.on_draw = False

            # Ｃ－１３）======= エイリアン軍団を移動する =======
            # Ｃ－１４）ループカウンタが、移動するタイミングの場合
            if loop_count % move_interval == 0:
                # Ｃ－１５）エイリアンの移動距離は仮に０としておく
                # move_x, move_y = 0, 0
                # エイリアンの範囲取得処理
                # エイリアンの1体を囲むような四角形を「エリア」としてコピーして取得
                area = aliens[0].rect.copy()
                # 全てのエイリアンに対して処理を行う
                for alien in aliens:
                    # そのエイリアンを四角に含むように、「エリア」を拡張する
                    area.union_ip(alien.rect)

                # 左移動フラグに応じて、移動方向(左右の移動距離)を決める
                move_x = -5 if is_left_move else 5
                move_y = 0

                # 「エリア」が左端または右端に到達して、下段移動していない場合
                if (area.left < 10 or area.right > 590) and not is_down_move:
                    # 左右移動フラグを逆にする
                    is_left_move = not is_left_move
                    # エイリアンの移動方向を、下に移動
                    move_x, move_y = 0, 24
                    # エイリアンの移動タイミングの感覚を2減らす(最小1)
                    move_interval = max(1, move_interval - 2)
                    # 下移動フラグをTrueにする
                    is_down_move = True
                else:
                    # 下移動フラグをFalseにする
                    is_down_move = False

                # Ｃ－１６）設定した移動距離に応じて、エイリアンを移動する
                for alien in aliens:
                    alien.move(move_x, move_y)

            # ショットが発射されている場合
            if shot.on_draw:
                # 自機ショットとエイリアンの衝突判定
                temp_aliens = []
                # エイリアンの数だけ繰り返す
                for alien in aliens:
                    # エイリアンの四角が自機ショットの中心と重なった場合
                    if alien.rect.collidepoint(shot.rect.center):
                        # 自機ショットを画面から消す
                        shot.on_draw = False
                        # スコアにエイリアンのスコアを加算する
                        score += alien.score
                    else:
                        # 撃たれてないエイリアンを、一時領域(temp_aliens)に追加する
                        temp_aliens.append(alien)
                # 一時領域のエイリアンリストを、新しいエイリアンリストにする
                aliens = temp_aliens
                # エイリアンリストが空になったら、クリア(ゲームオーバーにする)
                if len(aliens) == 0:
                    is_gameover = True

        # ======= 描画処理 =======
        surface.fill((0, 0, 0))
        ship.draw()  # 自機の描画
        shot.draw()
        # Ｃ－１７最後）エイリアン軍団の描画
        for alien in aliens:
            alien.draw()

        # スコアの描画
        score_str = str(score).zfill(5)
        score_image = scorefont.render(score_str, True, (0, 255, 0))
        surface.blit(score_image, (500, 10))

        # ゲーム終了時のメッセージの描画
        if is_gameover:
            # エイリアンがいない場合はクリアのメッセージ
            if len(aliens) == 0:
                msg_rect = msg_clear.get_rect()
                msg_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
                surface.blit(msg_clear, msg_rect.topleft)
            # エイリアンがいる場合はゲームオーバーのメッセージ
            else:
                msg_rect = msg_over.get_rect()
                msg_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
                surface.blit(msg_over, msg_rect.topleft)

        # 画面更新
        pygame.display.update()
        # 一定間隔の処理
        clock.tick(20)


if __name__ == "__main__":
    main()
