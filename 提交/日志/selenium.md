网页源代码与检查元素显示的内容不一样是一位动态加载不同（后者以JavaScript渲染）

初始HTML作为静态文件，后期访问后使用JavaScript动态渲染内容。requests库只能获取HTML，无法执行JS，必须模拟浏览器环境执行JS才能获取完整的HTML。

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import re

# Parse js code and get page content by selenium
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://news.sina.com.cn/roll/")

driver.implicitly_wait(5)

res_text = driver.page_source
driver.quit()

```

