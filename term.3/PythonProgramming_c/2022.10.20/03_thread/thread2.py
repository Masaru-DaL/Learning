from logging import getLogger, config
import sys
import yaml
import time
import threading
from inputwait import InputWait

with open('logconfig2.yaml', 'r') as yml:
    conf =  yaml.safe_load(yml)
 
#定義ファイルを使ったloggingの設定
config.dictConfig(conf)
#ロガーの生成
logger = getLogger("main")
# ログの出力
logger.info('..... Program Start .....')
# 入力待ちクラスのインスタンスを作成
iw = InputWait()
# 関数を対象として、スレッドのインスタンスを作成
input_thread = threading.Thread(target=iw.wait_routine)
# スレッドを開始
input_thread.start()

# 無限ループ
while True:
    # ログの出力
    logger.info('..... Timer Info .....')
    # タイマー（一定時間待つ）処理（0.5秒を指定）
    time.sleep(0.5)
    # 入力待ちクラスのフラグが終了になったら、終了
    if iw.is_finish:
        print("プログラムを終了します。")
        break

# ログの出力
logger.info('..... Program End .....')
