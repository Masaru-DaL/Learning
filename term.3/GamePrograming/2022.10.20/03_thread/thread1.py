from logging import getLogger, config
import sys
import yaml
import time
import threading

# 定義ファイルを使ったloggingの設定
with open("logconfig1.yaml", "r") as yml:
    conf = yaml.safe_load(yml)
config.dictConfig(conf)
# ロガーの生成
logger = getLogger("main")

# 数字入力関数
def input_num():

    ch = "a"
    while len(ch) != 0:
        try:
            # 入力待ち
            ch = input("数字を入力してください：")
            num = int(ch)
            # 結果の表示
            print(f"{num} が入力されました！")
            # ログの出力
            logger.info(f"入力された数字[{num}]")

        except ValueError as e:
            # ログの出力
            logger.error(e)
    print("処理を終了します")
    global is_finish
    is_finish = True


# グローバル変数: 終了フラグ
is_finish = False

# input_num関数を対象にして、スレッドのインスタンスを作成
input_thread = threading.Thread(target=input_num)
# スレッドの開始
input_thread.start()


# 最大100回の繰り返し
for _ in range(100):
    # 数字入力関数の呼び出し
    # input_num()
    # ログの出力
    logger.info("ループ処理の最後")
    # タイマー（一定時間待つ）処理（１秒を指定）
    time.sleep(1)
