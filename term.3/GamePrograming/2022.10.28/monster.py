import random
from game import Game, Phase
from character import Character
from monsterlist import MonsterList

# モンスタークラス
class Monster(Character):
    
    # コンストラクタ
    def __init__(self, pos, monster_no):
        # 親クラスのコンストラクタを呼び出し
        pass
        # モンスター番号を設定
        pass
        # モンスターの位置を設定（親クラスのメソッド）
        pass
        # モンスターの画像を作成＆設定
        pass
        # 名前
        pass
        # 攻撃力
        pass
        # 移動不能チップリスト
        pass
        # 移動インターバル
        pass
        # 移動方向変更タイミング
        pass
        # 移動後停止時間
        pass
        # 次移動開始時間
        pass
        # 移動方向
        pass
        # 残り移動回数
        pass

    # マップ移動チェック
    def check_map_move(self, posx, posy, dx, dy):
        # 右マップへ移動してしまう（一番右＋dxが正）
        pass
        # 左マップへ移動（一番左より左）
        pass
        # 下マップへ移動（一番下＋dyが正）
        pass
        # 上マップへ移動（一番上より上）
        pass

        return True

    # １フレームごとにする画像・処理
    def frame_process_img(self):
        
        # 移動中でない場合
        pass
            # 移動タイミングを超えている場合
        pass
                # 移動方向リスト
        pass
                # 移動方向をランダムに設定
        pass
                # 残り移動回数を設定
        pass
        # 移動中の場合
        pass
            # 移動タイミングを超えている場合
        pass
                # 上下左右キーが押されている場合にキャラを移動
                # 現在位置を取得
        pass
                # 移動方向に仮移動
        pass
                # 加算後の値で、位置を計算
        pass
                # マップ移動チェックで移動可能な場合
        pass
                    # 移動可能チェックで移動可能なら移動（不能なら位置を変更しない）
        pass
                # 残り移動回数を１減算
        pass
                # 移動回数が０になったら
        pass
                    # 次の移動タイミングを停止時間後に設定
        pass
                    # 移動方向をなしに
        pass
                    # 次の移動タイミングを設定
        pass
        
        # モンスターとプレイヤーの四角を取得
        pass
        # 重なった場合
        pass
            # モンスターを画面外に
            # （画面外に設定すると、移動チェックで出てこれなくなる…はず…）
        pass
            # プレイヤーのHPをモンスターの攻撃力分減らす
        pass
            # プレイヤーのHPが０以下になったら、フェイズをゲームオーバーにする
        pass
        
        # キャラクターの画像設定
        pass

