# 演習０
# 自分のチームと相手のチームとの対戦結果を持つクラス「match」を作成します
#
# このクラスでは以下のクラス変数を持ちます
# ・MY_TEAM … 自チームの名前（自由に決めてよい）
#   ※変数と言ってますが、これはプログラム中に変わらない定数です
#
# クラスに以下の関数を実装します
# ・コンストラクタ
#   引数に「相手のチーム名」を持ち、それをインスタンス変数に代入する
#   自チームの得点のインスタンス変数「my_score」を初期値「-1」で持つ
#   相手チームの得点のインスタンス変数「op_score」を初期値「-1」で持つ
#
# ・record_score（得点記録）
#   引数に「自チームの得点」「相手チームの得点」を持ち、
#   それらでインスタンス変数の値を更新する

# ・result_output（試合結果表示）
#   試合結果に応じて、チーム名、得点、勝ち負けを出力する
#   例１）勝ち、負け、引分の場合
#     負け キボガンズ 0－2 ヨコハマリン 勝ち
#     勝ち キボガンズ 2－1 コエビーナ 負け
#     引分 キボガンズ 1－1 フタマーズ 引分
#   例２）my_score が -1（試合未実施の場合）
#     未実施 キボガンズ － ヤマッツ

# 試合クラス
class Match:

    # チーム名のクラス変数（定数）
    MY_TEAM = "さいたまず"

    # コンストラクタ
    def __init__(self, op_team):
        self.op_team = op_team
        self.my_score = -1
        self.op_score = -1


    # 得点記録
    def record_score(self, my_s, op_s):
        self.my_score = my_s
        self.op_score = op_s

    # 試合結果表示
    def result_output(self):

        # ※出力するメッセージの例を用意しました。参考にして下さい
        if self.my_score == -1:
            print(f"未実施 {Match.MY_TEAM} － {self.op_team} ")
        elif self.my_score == self.op_score:
            print(f"引分 {Match.MY_TEAM} {self.my_score}－{self.op_score} {self.op_team} 引分")
        elif self.my_score > self.op_score:
            print(f"勝ち {Match.MY_TEAM} {self.my_score}－{self.op_score} {self.op_team} 負け")
        else:
            print(f"負け {Match.MY_TEAM} {self.my_score}－{self.op_score} {self.op_team} 勝ち")
