import os
import logging
from datetime import datetime

# 定义全局文件路径
LOG_FILE_PATH = os.path.join(os.getcwd(), "ahr999.log")
DATA_FILE_PATH = os.path.join(os.getcwd(), "ahr999_data.csv")

# 配置日志
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    filemode='a'  # 追加模式
)

def log_error(message):
    """
    记录错误日志
    """
    try:
        with open(LOG_FILE_PATH, "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ERROR: {message}\n")
        print(f"已记录错误日志: {message}")
    except Exception as e:
        print(f"记录日志时出错: {e}")
