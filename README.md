# BTC-Peak-Seller
每日 BTC 逃顶通知工具 BTC Peak Seller
该项目是一个使用 Selenium 爬取 AHR999 指标及相关数据的 Python 脚本，目标页面为 Coinglass AHR999 页面。脚本提取当前 AHR999 指标及日期等数据，并将其存储到 CSV 文件，同时通过日志记录调试信息和操作状态。
现已完成定时爬取以及发送信息的功能  

需要导入的库有 schdule requests webdriver webdriver_manager
以及需要使用edge浏览器最新版本  
# 功能：  
自动化数据爬取：使用 Selenium 获取 AHR999 指标数据。  
数据存储：将爬取的数据保存到 CSV 文件中，便于后续分析。  
日志记录：记录错误和操作状态，便于调试。  
无头模式：在后台运行，无需浏览器界面
定时获取：每日早上8点爬取数据
信息发送：定时发送到Telegram群内
# 所需环境：
Python 3.8 或更高版本  
必需的Python包：schdule requests webdriver webdriver_manager csv os logging  
Edge 浏览器：确保已安装 Microsoft Edge。  
EdgeDriver：Selenium 需要使用 EdgeDriver 与浏览器交互，脚本会通过 webdriver-manager 自动处理 EdgeDriver 的安装。
# 使用方法
直接运行脚本：  
`<python main.py>`  
控制台输出：确认数据已保存。  
`<开始保存数据...       数据保存成功>`
数据文件：更新 ahr999_data.csv，写入最新数据。  
日志文件：在 ahr999.log 中记录新的日志条目。  
# 常见问题排查

常见错误及解决方案

1.错误："Unable to obtain driver for chrome"

确保系统已安装 Edge 浏览器。

使用 webdriver-manager 自动安装 EdgeDriver。

2.错误："session not created: No matching capabilities found"

验证 Edge 浏览器版本是否与 EdgeDriver 兼容。

更新 Edge 浏览器到最新版本。

3.错误："未找到包含数据的标签"

确保目标网站的结构没有发生变化。

如果网站结构变动，请更新 fetch_untils.py 脚本中的 CSS 选择器。
