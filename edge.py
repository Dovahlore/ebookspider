# cmd "C:\Program Files (x86)\Microsoft\Edge Dev\Application\msedge.exe" --remote-debugging-port=9222 --user-data-dir="A:\dovahkiin\OneDrive - bupt.edu.cn\Projects\ebookspider\edgedriver_win32\python"
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import base64
import random
#用于选择登录端口
import time
from selenium.webdriver.edge.options import Options
#造浏览器配置对象
#通过百度页面，搜索烤鸭
print("connecting")
Edge_op = Options()
#配置浏览器
#"127.0.0.1:9222"其中，9222是浏览器的运行端口
Edge_op.add_experimental_option("debuggerAddress","127.0.0.1:9222")
#让浏览器带着这个配置运行
browser = Edge(options=Edge_op)
#测试环节
#通过百度页面，搜索烤鸭
print("linked to driver")
url=input("url input:")
browser.get(url)

print("ready to start？输入“y”开始")
while input()!='y':
    time.sleep(1)



i=0
print("url:",browser.current_url)
next_page = browser.find_element(By.CLASS_NAME, "swiper-button-next")
while True:
    try:
        canvas = browser.find_element(By.ID, "page%d"%i)
        # 找到 canvas 元素
        # 你可以对找到的 canvas 元素进行进一步操作，例如获取其大小
        width = canvas.get_attribute("width")
        height = canvas.get_attribute("height")
        print(f"canvas 元素的大小为：{width}x{height}")
        while width == "300" :
            width = canvas.get_attribute("width")
            height = canvas.get_attribute("height")
            time.sleep(5)


        i+=1

        # 使用 JavaScript 获取 canvas 的 data URL
        canvas_data_url = browser.execute_script("return arguments[0].toDataURL('image/jpeg');", canvas)

        # 解析出 base64 数据
        base64_image = canvas_data_url.split(',')[1]
        image_bytes = base64.b64decode(base64_image)

        # 将图片保存为文件
        with open("pic/page%d.jpg"%i, "wb") as image_file:
            image_file.write(image_bytes)
            print(f"已保存第{i}页图片")
        time.sleep(random.randint(4,8))
        actions = ActionChains(browser)

        actions.click(next_page)
        actions.perform()
        time.sleep(random.randint(8,10))# 300 表示移动的像素
    except Exception as e:
        print(e)
        break

#swiper-lazy swiper-lazy-loaded