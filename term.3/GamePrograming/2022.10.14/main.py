import sys
from random import randint
import pygame
from pygame.locals import Rect, QUIT, KEYUP, KEYDOWN, K_LEFT, K_RIGHT, K_SPACE
from drawable import Drawable, Ship, Beam, Shot, Alien

WINDOW_WIDTH = 600      # 画面の幅
WINDOW_HEIGHT = 600     # 画面の高さ
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
    
    keymap = []             # キーマップ
    is_gameover = False     # ゲームオーバーフラグ
    score = 0               # スコア
    aliens = []             # インベーダーのリスト
    beams = []              # ビームのリスト
    ship = Ship()           # 自機のインスタンス
    shot = Shot()           # 自機ショットのインスタンス

    # ======= メイン処理 =======
    while True:
        
        # イベント処理
        for event in pygame.event.get():
            # 終了処理
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        # ======= 描画処理 =======
        surface.fill((0, 0, 0))

        # スコアの描画
        score_str = str(score).zfill(5)
        score_image = scorefont.render(score_str,
                                       True, (0, 255, 0))
        surface.blit(score_image, (500, 10))

        # ゲーム終了時のメッセージの描画
        if is_gameover:
            # エイリアンがいない場合はクリアのメッセージ
            if len(aliens) == 0:
                msg_rect = msg_clear.get_rect()
                msg_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
                surface.blit(msg_clear, msg_rect.topleft)
            # エイリアンがいる場合はゲームオーバーのメッセージ
            else:
                msg_rect = msg_over.get_rect()
                msg_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
                surface.blit(msg_over, msg_rect.topleft)

        # 画面更新
        pygame.display.update()
        # 一定間隔の処理
        clock.tick(20)

if __name__ == '__main__':
    main()
