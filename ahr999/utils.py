import csv
import os
import logging
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager

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

def fetch_ahr999():
    logging.info("启动 Selenium for Edge...")
    try:
        # 设置 Edge 浏览器选项
        edge_options = Options()
        edge_options.add_argument("--headless")  # 无头模式（可选）
        edge_options.add_argument("--disable-gpu")  # 禁用 GPU 加速
        edge_options.add_argument("--no-sandbox")  # 在无沙盒模式下运行（Linux 必须）
        edge_options.add_argument("--disable-dev-shm-usage")  # 防止共享内存不足

        # 自动安装并配置 EdgeDriver
        service = Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=edge_options)

        logging.info("打开页面...")
        driver.get("https://www.coinglass.com/zh/pro/i/ahr999")

        # 检查页面标题，验证是否加载成功
        title = driver.title
        logging.info(f"页面标题: {title}")

        # 查找数据表的行和单元格
        table_row = driver.find_element(By.CSS_SELECTOR, "tr.ant-table-row.ant-table-row-level-0")
        date_td = table_row.find_element(By.CSS_SELECTOR, "td:nth-child(1) div")
        ahr_td = table_row.find_element(By.CSS_SELECTOR, "td:nth-child(2) div")

        # 获取数据
        date_text = date_td.text.strip()
        ahr_value = ahr_td.text.strip()

        logging.info(f"抓取结果: 日期={date_text}, AHR999={ahr_value}")
        driver.quit()
        return {"date": date_text, "ahr999": ahr_value}

    except Exception as e:
        logging.error(f"发生错误: {e}")

def save_data(data):
    print("开始保存数据...")
    try:
        # 如果文件不存在，则创建并写入表头
        if not os.path.exists(DATA_FILE_PATH):
            with open(DATA_FILE_PATH, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["日期", "AHR999 指标"])  # 写入表头

        # 追加数据到文件
        with open(DATA_FILE_PATH, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([data["date"], data["ahr999"]])  # 写入数据

        print("数据保存成功")
    except Exception as e:
        print(f"保存数据时出错: {e}")

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
