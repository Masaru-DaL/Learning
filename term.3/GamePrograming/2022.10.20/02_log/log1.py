import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="./logs/logfile01.log",
    format="%(asctime)s:[%(levelname)s] %(message)s",
    datefmt="%Y.%m.%d %H:%M:%S",
)

# ログを出力
logging.debug("Debugging information")
logging.info("Informational message")
logging.warning("Warning:config file %s not found", "server.conf")
logging.error("Error occurred")
logging.critical("Critical error -- shutting down")
