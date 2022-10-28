from game import Game
from square import Square

# フィールドチップクラス（画面１マスのクラス）
class Chip(Square):
    # コンストラクタ
    def __init__(self):
        # 親クラスのコンストラクタを呼び出す
        super().__init__()
        # チップ番号に初期値を設定
        self.chip_no = 0
        # チップ(フィールドの部品)の画像を読み込む
        self.images = (
            Game.read_image_for_square("image/chip0.png")
        )


    # チップ番号設定
    def set_chip_no(self, no):
        # 自身の持つ番号と、対応する画像を設定
        pass

    # 移動可能チェック
    def is_movable(self, unmovable_chip_list):
        # 移動不能チップの番号リストにない場合はTrueを返す
        pass
        return True
