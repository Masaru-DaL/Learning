import pygame
from game import Game, Phase
from field import Field
from player import Player
from monster import Monster
from monsterlist import MonsterList

# Pythonの基本処理
pygame.init()
Game.surface = pygame.display.set_mode([960, 640])
clock = pygame.time.Clock()
pygame.display.set_caption("*** Sample RPG ***")

# 描画用フォント（等幅フォントを使用しているので、使えなかったら変えてください）
smallfont = pygame.font.SysFont("Courier", 36)   # 小さい文字用のフォント
largefont = pygame.font.SysFont(None, 120)   # 大きい文字用のフォント

# ゲーム情報初期化処理
def init_game_info():
    # 各クラス変数に初期値を設定する
    is_gameover = False     # ゲームオーバーフラグ
    monsters = None         # モンスター
    # 仮に、フィールド表示をスタート状態とする（最終的にはタイトル画面にする）
    Game.phase = Phase.IN_FIELD
    # フィールドクラスのインスタンスを作成して、ゲームクラスの変数に設定
    Game.field = Field(Game.START_FIELD)
    # プレイヤークラスのインスタンスを作成して、ゲームクラスの変数に設定
    Game.player = Player()
    # モンスター（初期配置）
    pass

# 基本描画処理
def basic_draw():
    # フィールドの描画
    Game.field.draw()
    # モンスター達の描画
    pass
    # プレイヤーの描画
    Game.player.draw()
    # レベルの描画
    pass# 左空白埋めで５桁
    pass
    # HPの描画
    pass # 左空白埋めで５桁
    pass

# メイン処理
def main():
    # ゲーム情報の初期化処理を実行
    init_game_info()

    # ゲームのメインループ
    while True:
        # ゲームのカウンタを１加算
        Game.count += 1
        # イベントチェック処理（終了、キー入力）を実行
        Game.check_event()

        Game.surface.fill((0, 0, 0))    # 画面を黒で塗りつぶす
        # ===== ゲームフェーズによる処理段階分け =====
        # フィールド上の場合
        if Game.phase == Phase.IN_FIELD:
            # プレイヤーの毎回処理
            Game.player.frame_process_img()
            # モンスターの毎回処理
            pass
            # 基本描画処理
            basic_draw()

        # ゲームオーバーの場合
        pass
            # 基本描画処理
        pass
            # ゲームオーバーメッセージの描画
        pass

        pygame.display.update()     # 描画更新処理
        clock.tick(25)              # 一定時間処理

# メイン処理の呼び出し
if __name__ == '__main__':
    main()
