from logging import getLogger, config

# 数字入力クラス
class InputNum:
    
    def __init__(self):
        # モジュール用ロガーの生成
        self.logger = getLogger(__name__)
    
    def input_num(self):
        # ログの出力
        self.logger.info("input_num start")
        # インスタンス変数：入力OKフラグ
        self.is_ok_input = True

        try:
            # 入力待ち（入力文字をインスタンス変数に入れる）
            self.ch = input("数字を入力してください：")
            if self.ch != "":
                num = int(self.ch)
                # 結果の表示
                print(f"{num} が入力されました！")
                # ログの出力
                self.logger.info(f"入力された数字[{num}]")
            
        except ValueError as e:
            # ログの出力
            self.logger.error(e)
            # 入力OKフラグをFalseに
            self.is_ok_input = False
        
        # ログの出力
        self.logger.info("input_num end")

