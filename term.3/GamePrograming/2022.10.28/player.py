from game import Game
from character import Character

# プレイヤークラス
class Player(Character):

    # 移動不能チップの番号リスト（チップの番号と合わせること）
    UNMOVABLE_CHIP_LIST = [2, 3]
    # 初期レベル
    PLAYER_LV_1ST = 1
    # 初期ヒットポイント
    PLAYER_HP_1ST = 10

    # コンストラクタ
    def __init__(self):
        # 親クラスのコンストラクタを呼び出し
        super().__init__()
        # プレイヤーの位置を設定（親クラスのメソッド）
        self.set_pos(Game.START_PLAYER_POS_X, Game.START_PLAYER_POS_Y)
        # プレイヤーの画像を作成
        p1_images = (
            Game.read_image_for_square("image/hero1.png"),
            Game.read_image_for_square("image/hero2.png"),
        )
        # 画像を設定
        self.set_images(p1_images)
        # レベルを設定
        pass
        # ヒットポイントを設定
        pass

    # マップ移動チェック
    def check_map_move(self, posx, posy, dx, dy):
        pass
        # 右マップへ移動（一番右＋dxが正）
        pass
        # マップを右へ、プレイヤー位置を左へ
        pass
        # 左マップへ移動（一番左より左）
        pass
        # マップを左へ、プレイヤー位置を右へ
        pass
        # 下マップへ移動（一番下＋dyが正）
        pass
        # マップを下へ、プレイヤー位置を上へ
        pass
        # 上マップへ移動（一番上より上）
        pass
        # マップを上へ、プレイヤー位置を下へ
        pass

        # マップ変更後（変更してない場合も）の位置と変更フラグを返却
        return posx, posy, dx, dy, is_changed

    # １フレームごとにする画像・処理
    def frame_process_img(self):

        # 上下左右キーが押されている場合にキャラを移動
        # 現在位置を取得
        pass

        # それぞれのキーに合わせて、移動後の位置を設定
        pass
        # 加算後の値で、プレイヤーの位置を計算
        pass
        # マップ移動チェック
        pass
        # マップを変更していない場合
        pass
        # 移動可能チェックで移動可能なら移動（不能なら位置を変更しない）
        pass
        # マップを変更した場合は移動
        pass

        # キャラクターの画像設定
        self.set_chara_animation()
