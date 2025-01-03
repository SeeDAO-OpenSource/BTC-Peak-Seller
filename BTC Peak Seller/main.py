from config import log_error, DATA_FILE_PATH
from fetch_utils import fetch_ahr999
from telegram_utils import send_telegram_message
import os
import csv
import schedule
import time

def save_data(data):
    """
    保存数据到本地文件
    """
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

if __name__ == "__main__":
    # Telegram Bot 配置
    BOT_TOKEN = "7733661962:AAFBs_eeuR9nIDaE6C8-AW6zwT2_zSCKQgw"  # 替换为你的 Telegram 机器人令牌
    CHAT_ID = "-4638132702"      # 替换为你的 Telegram 聊天 ID

def scheduled_task():
    # 抓取 AHR999 数据
    data = fetch_ahr999()
    if data:
        # 保存数据到本地
        save_data(data)
        try:
            ahr999_value = float(data['ahr999'])
            if ahr999_value>1.200:
                # 格式化消息内容
                message = f"AHR999 指标更新：\n日期: {data['date']}\n数值: {data['ahr999']}\n注意：AHR999囤币指标已大于定投线！"
                # 发送消息到 Telegram
                send_telegram_message(BOT_TOKEN, CHAT_ID, message)
            else:
                log_error(f"AHR999 数值为 {ahr999_value}，小于等于 1.2，未发送至 Telegram。")
        except ValueError:
            log_error("AHR999 数值转换失败，无法比较大小。")
    else:
        log_error("未能抓取 AHR999 数据")

schedule.every().day.at("08:00").do(scheduled_task)

while True:
    schedule.run_pending()
    time.sleep(1)
