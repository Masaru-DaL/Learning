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
    # 隕石リスト
    stars = []
    # 押下キー
    keymap = []
    # 宇宙船の位置
    ship = [0, 0]
    # スコア
    score = 0
    # 宇宙船のスピード
    speed = 25
    
    # 画面表示用画像の読み込み
    scope_image = pygame.image.load("image/scope.png")
    rock_image = pygame.image.load("image/rock.png")
    # Ｅ－１）スコアとゲームオーバー用のフォントを用意
    scorefont = pygame.font.SysFont(None, 36)
    sysfont = pygame.font.SysFont(None, 72)
    # Ｅ－２）ゲームオーバー表示用
    message_over = sysfont.render("GAME OVER!!", True, (0, 255, 225))
    message_rect = message_over.get_rect()
    message_rect.center = (400, 400)

    # 隕石追加処理
    # 最大200個になるまで隕石を追加
    while len(stars) < 200:
        # 「pos」と「theta」というキーを持つ、辞書型として作成
        # 「pos」は隕石の座標を[x, y, z」で表したもの
        # 「theta」は隕石の見た目の回転度
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
            # キーが押された場合
            elif event.type == KEYDOWN:
                # そのキーが押下キーリストに入ってない場合追加する
                if not event.key in keymap:
                    keymap.append(event.key)
            # キーが離された場合
            elif event.type == KEYUP:
                # そのキーを押下キーリストから削除する
                keymap.remove(event.key)

        # ゲームオーバーでない場合
        if not is_gameover:
            # 押下されているキーに応じて、宇宙船の位置を移動
            # elifにしないことで斜め移動も可能にしている
            if K_LEFT in keymap:
                ship[0] -= 30
            if K_RIGHT in keymap:
                ship[0] += 30
            if K_UP in keymap:
                ship[1] -= 30
            if K_DOWN in keymap:
                ship[1] += 30
                
            # 宇宙船のx, y座標の範囲を-800から800にする
            ship[0] = max(-800, min(800, ship[0]))
            ship[1] = max(-800, min(800, ship[1]))
            
            # スコアを１加算
            score += 1
            # スピードは10ごとに１加算
            if score % 10 == 0:
                speed += 1
            # 隕石の位置を手前に移動
            for star in stars:
                # スピード分だけ手前に移動
                star["pos"][2] -= speed
                # Ｅ－３）隕石のz座標が64以下になったら、衝突チェックをする
                if star["pos"][2] < 64:
                    # Ｅ－４）x座標、y座標ともに差が50未満だったら
                    if abs(star["pos"][0] - ship[0]) < 50 and \
                        abs(star["pos"][1] - ship[1]) < 50:
                        # Ｅ－５）ゲームオーバーフラグをTrueにする
                        is_gameover = True
                        # Ｅ－６）デバッグ用に位置を出力
                        print(f"{star['pos']=},{ship=}")
                    # Ｅ－７）ぶつかっていなかったら、隕石の位置をリセット
                    else:
                        star["pos"] = [randint(-1600, 1600),
                                    randint(-1600, 1600), 4095]
                    # star["pos"] = [randint(-1600, 1600),
                    #             randint(-1600, 1600), 4095]
                
        # 背景を黒で描画
        surface.fill((0, 0, 0))
        #これを追加するまえに、一度実行して確認する
        #奥の隕石ほど先に描画するように、z座標が大きい物が先にくるようにソートする
        stars = sorted(stars, key=lambda z: z["pos"][2], reverse=True)
        # 隕石の描画
        for star in stars:
            # 隕石の位置を取得
            # 宇宙船との位置との相対的な位置にする
            # 遠くの位置にあるものは内側に出てくるように、x, y座標を
            # z座標（奥行）をもとに算出
            # ※(50 << 9) は左に９ビットシフト＝512倍と同じ）
            # 最後に、x, y 方向の座標位置を400加算して調整する（中心をずらす）
            zpos = star["pos"][2]
            #xpos = (star["pos"][0] << 9) / zpos + 400
            #ypos = (star["pos"][1] << 9) / zpos + 400
            xpos = ((star["pos"][0] - ship[0]) << 9) / zpos + 400
            ypos = ((star["pos"][1] - ship[1]) << 9) / zpos + 400

            # シフト演算で計算しつつ、隕石のサイズ割合を計算
            size = (50 << 9) / zpos
            # 隕石を回転、縮小した画像を作成（サイズはさらに145で割って調整）
            rotated_rock = pygame.transform.rotozoom(rock_image,
                                    star["theta"], size / 145)
            # 隕石を描画
            surface.blit(rotated_rock, (xpos, ypos))
        
        # 宇宙船内部の描画
        surface.blit(scope_image, (0, 0))
        # Ｅ－８）ゲームオーバーの場合、メッセージを表示
        if is_gameover:
            surface.blit(message_over, message_rect)

        # Ｅ－９）スコアの描画
        score_str = str(score).zfill(6)     # Ｅ－１０：最後）０で埋めて６桁にする
        score_image = scorefont.render(score_str, True, (0, 255, 0))
        surface.blit(score_image, (700, 50))
        
        # 画面描画の更新
        pygame.display.update()
        # 一定のタイミングでループする
        clock.tick(20)

# メイン処理呼び出し
if __name__ == '__main__':
    main()
