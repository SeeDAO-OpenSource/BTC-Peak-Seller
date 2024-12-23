from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import logging

def fetch_ahr999():
    """
    爬取 AHR999 指标数据
    """
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
        return None
