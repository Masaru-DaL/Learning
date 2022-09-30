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
    # Ｂ－１）隕石リスト
    stars = []
    # 画面表示用画像の読み込み
    scope_image = pygame.image.load("image/scope.png")
    rock_image = pygame.image.load("image/rock.png")
    
    # Ｂ－２）隕石追加処理
    # Ｂ－２）最大200個になるまで隕石を追加
    while len(stars) < 200:
        # Ｂ－３）「pos」と「theta」というキーを持つ、辞書型として作成
        # Ｂ－３）「pos」は隕石の座標を[x, y, z」で表したもの
        # Ｂ－３）「theta」は隕石の見た目の回転度
        stars.append({
            "pos": [randint(-1600, 1600),
                    randint(-1600, 1600), randint(0, 4095)],
            "theta": randint(0, 360)
        })
    
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
        
        # Ｂ－４）隕石の描画
        for star in stars:
            # Ｂ－５）隕石の位置を取得
            # Ｂ－５）遠くの位置にあるものは内側に出てくるように、x, y座標を
            # Ｂ－５）z座標（奥行）をもとに算出
            # Ｂ－５）※(50 << 9) は左に９ビットシフト＝512倍と同じ）
            # Ｂ－５）最後に、x, y 方向の座標位置を400加算して調整する（中心をずらす）
            zpos = star["pos"][2]
            xpos = (star["pos"][0] << 9) / zpos + 400
            ypos = (star["pos"][1] << 9) / zpos + 400
            # Ｂ－６）シフト演算で計算しつつ、隕石のサイズ割合を計算
            size = (50 << 9) / zpos
            # Ｂ－７）隕石を回転、縮小した画像を作成（サイズはさらに145で割って調整）
            rotated_rock = pygame.transform.rotozoom(rock_image,
                                    star["theta"], size / 145)
            # Ｂ－８：最後）隕石を描画
            surface.blit(rotated_rock, (xpos, ypos))
        
        # 宇宙船内部の描画
        surface.blit(scope_image, (0, 0))

        # 画面描画の更新
        pygame.display.update()
        # 一定のタイミングでループする
        clock.tick(20)

# メイン処理呼び出し
if __name__ == '__main__':
    main()
