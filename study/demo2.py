# python小案列：利用爬虫获取知乎网站图片并下载到本地
# 注意事项：1.安装完webdriver后，还需要下载谷歌浏览器驱动 https://sites.google.com/a/chromium.org/chromedriver/ ，注意下载浏览器版本对应的驱动。
#           2.将下载好的chromedriver.exe 放到python的Scripts文件夹下。
import re
from selenium import webdriver
import time
import urllib.request
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.zhihu.com/question/29134042")
i = 0
while i < 10:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    try:
        driver.find_element_by_css_selector('button.QuestionMainAction').click()
        print("page" + str(i))
    except:
        break
result_raw = driver.page_source
content_list = re.findall('img src="(.+?)" ',str(result_raw))
n = 0
while n < len(content_list):
    i = time.time()
    local = (r"%s.jpg" % (i))
    urllib.request.urlretrieve(content_list[n], local)
    print("编号：" + str(i))
    n = n + 1