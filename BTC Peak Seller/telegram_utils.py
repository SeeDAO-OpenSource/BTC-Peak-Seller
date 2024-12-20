import requests

def send_telegram_message(bot_token, chat_id, message):
    """
    使用 Telegram Bot API 向指定的聊天发送消息。

    参数：
    - bot_token (str): Telegram 机器人令牌。
    - chat_id (str): 聊天 ID。
    - message (str): 要发送的消息内容。
    """
    # Telegram API 的 URL，用于发送消息
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    # 请求的参数，包含 chat_id 和消息内容
    payload = {
        'chat_id': chat_id,  # 聊天 ID
        'text': message      # 消息内容
    }

    try:
        # 发送 POST 请求到 Telegram API
        response = requests.post(url, data=payload)

        # 检查响应状态码是否为 200（成功）
        if response.status_code == 200:
            print("消息发送成功！")
        else:
            print(f"消息发送失败，状态码：{response.status_code}")
            print("响应内容：", response.text)

    except Exception as e:
        # 捕获异常并打印错误信息
        print("发送消息时发生错误：", str(e))
