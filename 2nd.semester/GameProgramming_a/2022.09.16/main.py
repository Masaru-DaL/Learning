import sys
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from random import randint

# タイルの横方向、縦方向の数
TILE_COUNT_X = 20
TILE_COUNT_Y = 15
# タイルの幅、高さ
TILE_WIDTH = 50
TILE_HEIGHT = 50
# 設置する爆弾の数
SET_BOMB_COUNT = 20
# タイルの状態（空、爆弾、オープン済み）
TILE_STATUS_EMPTY = 0
TILE_STATUS_BOMB = 1
TILE_STATUS_OPENED = 2
# 数字表示用の文字リスト
DISP_NUMBERS = ["","１","２","３","４","５","６","７","８"]
# クリア、ゲームオーバーのメッセージ
MSG_CLEAR = "クリアー！"
MSG_GAMEOVER = "ゲームオーバー"
# 各描画の色
COLOR_BG = (0, 0, 0)
COLOR_TILE = (192, 192, 192)
COLOR_LINE = (96, 96, 96)

COLOR_NUM = (255, 255, 0)
COLOR_BOMB = (255, 100, 100)
COLOR_MSG_CLEAR = (0, 0, 255)
COLOR_MSG_GAMEOVER = (255, 0, 0)

open_count = 0  # オープン済みタイル数
# チェック済みタイルリスト（２重のリスト）をすべて「False」で作成する
checked_tiles = [[False for x in range(TILE_COUNT_X)] for y in range(TILE_COUNT_Y)]

# Pygameの初期化処理等
pygame.init()
surface = pygame.display.set_mode([TILE_WIDTH * TILE_COUNT_X, TILE_HEIGHT * TILE_COUNT_Y])
clock = pygame.time.Clock()

# -------------- 周囲の爆弾の数を数える --------------
def count_bombs(field, x_pos, y_pos):
    count = 0 # 爆弾の数の初期化
    # 現在の位置から見て周囲9タイルが爆弾かどうかを相対パスで調べる。
    # 自身のタイルも含むが、爆弾ではないはずなのでそのまま数える(爆弾ではない前提)
    # offset -> 相対という意味で変数名に付ける
    for y_offset in range(-1, 2):
        for x_offset in range(-1, 2):
            # 相対位置から、タイルの位置を算出
            x = x_pos + x_offset
            y = y_pos + y_offset
            # タイルが画面内の場合(未満とすることで1個手前(はみ出さない位置)を意味する)
            if 0 <= x < TILE_COUNT_X and 0 <= y < TILE_COUNT_Y:
                # タイルが爆弾の場合、爆弾の数を1加算
                if field[y][x] == TILE_STATUS_BOMB:
                    count += 1
    # 数えた爆弾の数を戻り値にする
    return count


# -------------- タイルのオープン処理 --------------
def open_tile(field, x_pos, y_pos):
    global open_count
    # 街灯の箇所をオープン済みにする処理
    field[y_pos][x_pos] = TILE_STATUS_OPENED
    # オープン済みタイル数を1増やす
    open_count += 1
    # 現在の位置の周囲の爆弾数を数える
    count = count_bombs(field, x_pos, y_pos)
    # 周囲の爆弾数が1より大きいなら、関数を終了する
    if count > 0:
        return

    # 現在の位置から周囲9マスを相対パスでオープンする
    for y_offset in range(-1, 2):
        for x_offset in range(-1, 2):
            # 相対位置から、タイルの位置を算出
            x = x_pos + x_offset
            y = y_pos + y_offset
            # タイルが画面内の場合(未満とすることで1個手前(はみ出さない位置)を意味する)
            if 0 <= x < TILE_COUNT_X and 0 <= y < TILE_COUNT_Y:
                # その位置のタイルをオープン済みにする
                field[y][x] = TILE_STATUS_OPENED


# -------------- メイン処理 --------------
def main():
    # フォントを２種類用意
    # 日本語フォントを使うためには、SysFont ではなくFontで、
    # フォントファイルの置いてあるパスを指定します
    # ゲームを配布する場合は、フォント（配布可能なもの）も合わせて配布すると良いでしょう
    # 参考サイト例（https://helpx.adobe.com/jp/x-productkb/global/cq08041028.html）
    # small_font = pygame.font.Font("C:/Windows/Fonts/meiryo.ttc", 42)
    # large_font = pygame.font.Font("C:/Windows/Fonts/meiryo.ttc", 120)
    small_font = pygame.font.Font("C:/Windows/Fonts/HGRGY.TTC", 42)
    large_font = pygame.font.Font("C:/Windows/Fonts/HGRGY.TTC", 120)
    msg_clear = large_font.render(MSG_CLEAR, True, COLOR_MSG_CLEAR)
    msg_gameover = large_font.render(MSG_GAMEOVER, True, COLOR_MSG_GAMEOVER)
    # ゲームオーバーフラグの初期値をFalseにする
    is_gameover = False
    # フィールドの情報リスト(2重リスト)をすべて「空」で作成する
    field = [[TILE_STATUS_EMPTY for x in range(TILE_COUNT_X)] for y in range(TILE_COUNT_Y)]

    ###### 爆弾設置処理 ######
    count = 0 # 設置した爆弾数の初期化
    while True:
        # 設置位置をランダムで取得(-1の処理はrangeと違って最後の数も取るため)
        xpos = randint(0, TILE_COUNT_X - 1)
        ypos = randint(0, TILE_COUNT_Y - 1)
        # 設置位置が「空」だったら
        # この処理を行わないと、爆弾のある位置に爆弾を置いてしまうということが起きてしまう=設置位置が爆弾じゃない、としても多分大丈夫
        if field[ypos][xpos] == TILE_STATUS_EMPTY:
            # 爆弾を設置して、設置済み爆弾数を1増やす
            field[ypos][xpos] = TILE_STATUS_BOMB
            count += 1
        # 設置爆弾数が定数の「設置する爆弾の数」になったら処理を終了する
        if count == SET_BOMB_COUNT:
            break

    ###### メイン繰り返し処理 ######
    while True:

        ### イベント処理 ###
        for event in pygame.event.get():
            # 終了イベント処理
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # マウス左クリック処理
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                # クリック位置に応じて、タイルの位置を取得
                xpos = event.pos[0] // TILE_WIDTH
                ypos = event.pos[1] // TILE_HEIGHT
                # クリックされた位置が「爆弾」だったらゲームオーバー処理
                if field[ypos][xpos] == TILE_STATUS_BOMB:
                    is_gameover = True
                # クリックされた位置が「爆弾以外」だったらタイルオープン処理
                # else -> オープン済みだったらもう一度オープンする(支障無し)
                else:
                    open_tile(field, xpos, ypos)


        ### 描画 ###
        surface.fill(COLOR_BG)

        for ypos in range(TILE_COUNT_Y):
            for xpos in range(TILE_COUNT_X):
                # その位置のタイルの情報を取得
                tile_status = field[ypos][xpos]
                # タイル描画用の四角形情報(四角形の左上のx座標、四角形の左上のy座標、縦幅、横幅)
                rect = (xpos * TILE_WIDTH, ypos * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT)
                # タイルが「空」か「爆弾」の場合
                if tile_status == TILE_STATUS_EMPTY or tile_status == TILE_STATUS_BOMB:
                    # タイルを描画する(画面、色、位置)
                    pygame.draw.rect(surface, COLOR_TILE, rect)
                    # ゲームオーバーで、タイルが「爆弾」の場合
                    if is_gameover and tile_status == TILE_STATUS_BOMB:
                        # 爆弾を描画
                        pygame.draw.ellipse(surface, COLOR_BOMB, rect)
                # タイルが「オープン済み」の場合
                elif tile_status == TILE_STATUS_OPENED:
                    # 周囲の爆弾数をカウントする
                    count = count_bombs(field, xpos, ypos)
                    # 周囲の爆弾数が1以上の場合
                    if count > 0:
                        # 数字を描画する
                        num_image = small_font.render(DISP_NUMBERS[count], True, COLOR_NUM)
                        # 起点が左上で指定するが、若干ずれるため、真ん中に数字を描画するために微調整が必要
                        # フォントによっても表示される位置が違う
                        surface.blit(num_image, (xpos * TILE_WIDTH + 5, ypos * TILE_HEIGHT + 4))





        # 線の描画: 縦線
        for index in range(0, TILE_COUNT_X * TILE_WIDTH, TILE_WIDTH):
            pygame.draw.line(surface, COLOR_LINE,
                            # TILE_COUNT_Y * TILE_HEIGHT -> 15*50(定数値)
                            (index, 0), (index, TILE_COUNT_Y * TILE_HEIGHT))

        # 線の描画: 横線
        for index in range(0, TILE_COUNT_Y * TILE_HEIGHT, TILE_HEIGHT):
            pygame.draw.line(surface, COLOR_LINE,
                            # TILE_COUNT_X * TILE_WIDTH -> 20*50(定数値)
                            (0, index), (TILE_COUNT_X * TILE_WIDTH, index))

        # ゲームオーバーの場合
        if is_gameover:
            # メッセージ領域の四角形を取得し、その中央の位置を設定する
            msg_rect = msg_gameover.get_rect()
            msg_rect.center = (TILE_COUNT_X * TILE_WIDTH / 2, TILE_COUNT_Y * TILE_HEIGHT / 2)
            surface.blit(msg_gameover, msg_rect.topleft)

        # 画面の更新
        pygame.display.update()
        # 一定周期での繰り返し
        clock.tick(15)

# メイン関数の呼び出し
if __name__ == '__main__':
    main()
