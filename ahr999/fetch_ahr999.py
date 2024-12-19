from utils import fetch_ahr999, save_data


def main():
    print("开始爬取 AHR999 数据...")
    try:
        # 调用爬取函数
        data = fetch_ahr999()

        # 检查是否成功获取到数据
        if data:
            print(f"爬取数据成功：{data}")
            save_data(data)  # 保存数据到文件
        else:
            print("未获取到数据，请检查目标页面结构或请求状态")
    except Exception as e:
        print(f"爬取过程中发生错误: {e}")


if __name__ == "__main__":
    main()
