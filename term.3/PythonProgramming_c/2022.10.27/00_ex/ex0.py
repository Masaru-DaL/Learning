from logging import getLogger, config
import sys
import yaml
import time
import threading

# 定義ファイルを使ったloggingの設定
with open('ex0_log.yaml', 'r') as yml:
    conf =  yaml.safe_load(yml)
config.dictConfig(conf)
# ロガーの生成
logger = getLogger("main")

# 文字入力関数
def input_str():
    global input_ch
    while len(input_ch) != 0:
        # 入力待ち
        input_ch = input("文字を入力してください：")
        # 結果の表示
        print(f"{input_ch} が入力されました！")
        # ※演習０）入力された文字をログに出力する
        logger.info(f"入力された文字【{input_ch}】")

# 入力文字用グローバル変数
input_ch = "aaaa"   # 空だと終了してしまうので、何かを設定しておく

# ※演習０）関数を対象として、スレッドのインスタンスを作成する
input_thread = threading.Thread(target = input_str)
# ※演習０）スレッドの開始
input_thread.start()

while len(input_ch) != 0:
    # ※演習０）ログの出力をする（ターミナルに出ているものをログに出す）
    logger.info('[一定時間ログ]')
    # タイマー（一定時間待つ）処理（0.5秒を指定）
    time.sleep(0.5)
