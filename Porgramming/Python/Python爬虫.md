获取列表网页

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import re

# Parse js code and get page content by selenium

# Options for webdriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Request url page content
driver.get("https://news.sina.com.cn/roll/")

driver.implicitly_wait(5)

res_text = driver.page_source
driver.quit()
```





正则表达式解析所有链接

```python
# Get news list by regenx

# Define a pattern by regenx
pattern = r"https://finance\.sina\.com\.cn/[a-zA-Z0-9/_-]+/doc-[a-zA-Z0-9]+\.shtml"
news_list = re.findall(pattern, res_text)

print('\n'.join(news_list)) # Print the list
```

