import logging
from logging import getLogger
import sys

# ロガーの生成
logger = getLogger(sys.argv[0])
# 出力レベルの設定
logger.setLevel(logging.DEBUG)


# フォーマッタ
# loggerのフォーマット、出力先ファイルを定義
formatter = logging.Formatter(
    "%(asctime)s:[%(levelname)s]<%(name)s> %(message)s",
)
file_handler = logging.FileHandler("logs/logfile02.log")
file_handler.setFormatter(formatter)

# loggerのフォーマット、出力先ファイルを設定
logger.addHandler(file_handler)

# ログの出力
logger.debug("debug message")
logger.error("message")
