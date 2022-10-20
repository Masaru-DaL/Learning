from logging import getLogger, config
import time
import threading
from inputnums import InputNum

# 入力待ちクラス
class InputWait:
    def __init__(self):
        # モジュール用ロガーの生成
        self.logger = getLogger(__name__)
        
    def wait_routine(self):
        # ログの出力
        self.logger.info("wait_routine start")
        # インスタンス変数：終了フラグ
        self.is_finish = False
        
        while True:
            # 数字入力クラスのインスタンスを作成
            inn = InputNum()
            # 関数を対象として、スレッドのインスタンスを作成
            input_thread = threading.Thread(target=inn.input_num)
            # スレッドの開始
            input_thread.start()
            # ログの出力
            self.logger.info("Call [input_num]")
            # スレッドが終わるのを待つ
            input_thread.join()
            # ログの出力
            self.logger.info("Finish [input_num]")
            
            # もしエラーがあった場合は入力を５秒待つ
            if not inn.is_ok_input:
                print("数字以外が入力されました！ しばらくお待ち下さい…")
                time.sleep(5)
            # 空が入力されたら終了
            if inn.ch == "":
                self.is_finish = True
                break
        # ログの出力
        self.logger.info("wait_routine end")
