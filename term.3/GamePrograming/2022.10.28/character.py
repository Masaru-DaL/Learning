from game import Game
from square import Square

# キャラクタークラス（プレイヤーとモンスターの共通的な部分のクラス）
class Character(Square):
    
    # 画像を変える間隔
    CHANGE_IMAGE_INTERVAL = 10
    # キャラクターの移動距離
    MOVE_STEP = 16
    
    # コンストラクタ
    def __init__(self):
        # 親クラスのコンストラクタを呼び出し
        pass
        # 画像リスト
        pass
        # 画像変更タイミング
        pass

    # 画像リスト設定
    def set_images(self, image_list):
        pass
        # 画像を設定
        pass

    # キャラクターの位置を計算
    def calc_chara_pos(self, posx, posy, dx, dy):
        # スクエアに対する端数が１スクエア分を超える
        # またはマイナスになる場合に値を調整
        pass

    # キャラクター移動チェック
    def check_chara_move(self, posx, posy, dx, dy, unmovable_chip_list):
        check_pos_list = []         # チェック位置リスト
        # チェック対象に、移動先のposx, posyを追加
        pass
        # もし、上下方向にずれがある場合、ひとつ下のマスもチェック対象に追加
        pass
        # もし、左右方向にずれがある場合、ひとつ右のマスもチェック対象に追加
        pass
        # もし、両方にずれがある場合、右下のマスもチェック対象に追加
        pass
        # フィールドクラスのチェックを実施し、その結果を戻り値に設定
        pass

    # キャラクターの画像（アニメーション）設定
    def set_chara_animation(self):
        # 画像を変えるタイミングの場合、画像を変更
        pass
            # 画像番号を１加算して、画像の数を超えた場合０に戻す
        pass
            # 親クラス（Square）の画像を設定
        pass
            # 次の画像変更タイミングを設定
        pass


