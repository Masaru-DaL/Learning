from logging import getLogger, config
import sys
import yaml

# yaml はインストールとインポートが必要
# pip install pyyaml

# ログ設定ファイルをYAML形式で読み込み
with open("logconfig.yaml", "r") as log_info_file:
    conf = yaml.safe_load(log_info_file)

# 定義ファイル（辞書ファイル）を使ったloggingの設定
config.dictConfig(conf)

# ロガーの生成
logger = getLogger("main")

# ログの出力
logger.debug("Debugging information")
logger.info("Informational message")
logger.warning("Warning:config file %s not found", "server.conf")
logger.error("Error occurred")
logger.critical("Critical error -- shutting down")
