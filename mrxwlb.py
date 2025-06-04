import os, urllib, calendar, base64
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.print_page_options import PrintOptions

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("load-extension=C:/Users/win11/AppData/Local/Google/Chrome/User Data/Default/Extensions/bgnkhhnnamicmpeenaelnjfhikgbkllg/5.0.217_0") # 添加本地插件
chrome_options.add_argument('--headless') #headless模式下，浏览器窗口不可见，可提高效率（无头模式加载的插件必须是本地已安装的插件）
chrome_options.add_argument("--ignore-ssl-errors") #忽略 SSL 错误


current_directory = os.path.dirname(os.path.abspath(__file__) ) #设置默认保存路径为当前目录
chromedriver_path = '{}/chromedriver.exe'.format(current_directory)

driver = webdriver.Chrome(service = Service(chromedriver_path), options = chrome_options)
driver.maximize_window()
driver.set_page_load_timeout(20) #设置页面加载超时时间

print_options = PrintOptions() #配置打印选项

for month in range(12, 12 + 1):
    days = calendar.monthrange(2025, month)[1] #数组的第二个位置为月份的天数
    for day in range(1, days + 1):
        title = '2025年{:02d}月{:02d}日新闻联播文字版'.format(month, day)
        url = 'http://mrxwlb.com/2025/{:02d}/{:02d}/{}/'.format(month, day, urllib.parse.quote(title))

        driver.get(url)
        pdf = driver.print_page(print_options)
        with open('{}/{}.pdf'.format(current_directory, title), 'wb') as file: #写入文件
            file.write(base64.b64decode(pdf))

driver.quit() #关闭浏览器
