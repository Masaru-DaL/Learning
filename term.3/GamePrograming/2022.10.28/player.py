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
        is_changed = False  # マップ変更フラグ
        # 右マップへ移動（一番右＋dxが正）
        if posx == Game.FIELD_WIDTH - 1 and dx > 0:
            # マップを右へ、プレイヤー位置を左へ
            Game.field.change_field(1, 0)
            posx, dx = 0, 0
            is_changed = True
        # 左マップへ移動（一番左より左）
        if posx < 0:
            # マップを左へ、プレイヤー位置を右へ
            Game.field.change_field(-1, 0)
            posx, dx = Game.FIELD_WIDTH - 1, 0
            is_changed = True

        # 下マップへ移動（一番下＋dyが正）
        if posy == Game.FIELD_HEIGHT - 1 and dy > 0:
            # マップを下へ、プレイヤー位置を上へ
            Game.field.change_field(0, 1)
            posy, dy = 0, 0
            is_changed = True
        # 上マップへ移動（一番上より上）
        if posy < 0:
        # マップを上へ、プレイヤー位置を下へ
            Game.field.change_field(0, -1)
            posy, dy = Game.FIELD_HEIGHT - 1, 0
            is_changed = True

        # マップ変更後（変更してない場合も）の位置と変更フラグを返却
        return posx, posy, dx, dy, is_changed

    # １フレームごとにする画像・処理
    def frame_process_img(self):

        # 上下左右キーが押されている場合にキャラを移動
        # 現在位置を取得
        posx, posy = self.get_pos()
        dx, dy = self.get_dpos()

        # それぞれのキーに合わせて、移動後の位置を設定
        if Game.on_downkey():
            dy += Character.MOVE_STEP
        elif Game.on_upkey():
            dy -= Character.MOVE_STEP
        elif Game.on_rightkey():
            dx += Character.MOVE_STEP
        elif Game.on_leftkey():
            dx -= Character.MOVE_STEP

        # 加算後の値で、プレイヤーの位置を計算
        posx, posy, dx, dy = self.calc_chara_pos(posx, posy, dx, dy)
        # マップ移動チェック
        posx, posy, dx, dy, is_changed = self.check_map_move(posx, posy, dx, dy)
        # マップを変更していない場合
        if not is_changed:
            # 移動可能チェックで移動可能なら移動（不能なら位置を変更しない）
            if self.check_chara_move(posx, posy, dx, dy, Player.UNMOVABLE_CHIP_LIST):
                self.set_pos(posx, posy)
                self.set_dpos(dx, dy)
        # マップを変更した場合は移動
        else:
            self.set_pos(posx, posy)
            self.set_dpos(dx, dy)


        # キャラクターの画像設定
        self.set_chara_animation()
