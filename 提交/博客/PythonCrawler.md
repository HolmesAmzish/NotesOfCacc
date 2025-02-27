---
file: PythonCrawler.md
title: Python 爬虫
date: 2025-02-09 10:38
author: Holmes Amzish
tags: ['crawler', 'python']
---

# 爬虫的背景与应用

## 诞生

爬虫（Web Crawling）是自动化程序，用于从互联网上获取信息。爬虫的基本任务是自动访问网站，通过抓取网页内容并提取有用数据来构建数据库、索引或者进行进一步的数据分析。爬虫通常会模拟浏览器的行为，以避免被服务器识别为机器人，并且能够在大规模范围内高效地抓取信息。

爬虫技术最早由搜索引擎开发者提出，目的是自动收集网页信息并将其索引，便于用户搜索时快速检索相关内容。随着互联网的快速发展，网页内容的增长也越来越迅速，手动收集和分析数据的难度增加，爬虫技术逐渐成为获取网络数据的标准方法。

## 技术原理

爬虫通常通过以下几个步骤实现数据抓取：

1. **发送HTTP请求**：爬虫向目标网站的服务器发送请求，获取网页的HTML源代码或API数据。
2. **解析网页内容**：根据页面的结构（如HTML、JSON），爬虫提取有用的信息。常用的解析工具包括BeautifulSoup（用于HTML）、lxml等。
3. **数据存储**：抓取的数据可以存储在不同的地方，常见的存储方式有CSV、数据库（如MySQL、MongoDB）、NoSQL数据库等。
4. **处理反爬机制**：为了防止恶意抓取，许多网站会设置反爬机制，如验证码、IP封禁、请求频率限制等。爬虫需要使用一些技巧规避这些限制，如使用代理、模拟浏览器行为、动态延迟等。



例如，有如下网页：

```html
<!doctype html>
<html lang="en-US">
<head>
    <meta charset="utf-8" />
    <title>Simple DOM example</title>
</head>
<body>
<section>
    <img src="/icon.jpg" alt="Logo" width=30%>
    <p>
        Here we will add a link to the
        <a href="https://www.mozilla.org/">Mozilla homepage</a>
    </p>
</section>
</body>
```

通过 Python 脚本发送请求获取到 HTML 代码后，通过筛选元素，例如如果需要爬取图片，就对代码中的 img 元素进行筛选，同理段落元素则筛选出 p 元素，这是 BeautifulSoup 的爬取规则。当然原始的方法还有通过正则表达式进行匹配。

其次，爬虫除了下载指定页面内容外，还可以通过访问本页指向的其他地址进行爬取，例如筛选出上文的 a 元素并将 href 属性存入程序中以供接下来爬取，这样就实现了爬虫的自动化。使用者提供的最初的网页被称为根，而爬虫不断爬取页面其他链接的数量称为深度。



# 详细操作

## 需求分析

这里以爬取新浪新闻为例，新浪新闻的滚动新闻页面直接可以展示出许多新闻链接，类似于导航，可以作为比较好的根网站。首先通过滚动页面解析出所有的新闻链接，然后对所有链接的新闻进行爬取，并存入本地数据库中。

数据库采用 SQLite，一个小型本地数据库。数据库以一个 db 文件形式存在本地。



## 请求内容

### requests

```python
import requests

url = "https://finance.sina.com.cn/roll/#pageid=384&lid=2519&k=&num=50&page=1"

response = requests.get(url)

print(response.status_code) # 200，表示成功
if response.status_code == 200:
    content = response.text
    print(content)
```

可以看到有一部分内容如下，这些链接就是需要爬取的内容网站：

```
<li><a href="https://cj.sina.cn/article/norm_detail?url=https%3A%2F%2Ffinance.sina.com.cn%2Fstock%2Fusstock%2Fc%2F2025-02-08%2Fdoc-ineiumza6406789.shtml" target="_blank">
	沃尔沃汽车将几乎零成本收购Northvolt电池合资企业股份
</a></li>
						
<li><a href="https://cj.sina.cn/article/norm_detail?url=https%3A%2F%2Ffinance.sina.com.cn%2Fstock%2Fbxjj%2F2025-02-08%2Fdoc-ineiumza6402728.shtml" target="_blank">
	小心“李鬼”！你炒的DeepSeek概念股可能是假的
</a></li>
						
<li><a href="https://cj.sina.cn/article/norm_detail?url=https%3A%2F%2Ffinance.sina.com.cn%2Froll%2F2025-02-08%2Fdoc-ineiumyy8907788.shtml" target="_blank">
	马斯克战胜美国最大工会！美法官拒绝阻止DOGE访问劳工部系统
</a></li>

<li><a href="https://cj.sina.cn/article/norm_detail?url=https%3A%2F%2Ffinance.sina.com.cn%2Fjryx%2Fbank%2F2025-02-08%2Fdoc-ineiumyx2131162.shtml" target="_blank">
	建设银行上海市金山石化支行被罚40万元：因贷款业务严重违反审慎经营规则
</a></li>

<li><a href="https://cj.sina.cn/article/norm_detail?url=https%3A%2F%2Ffinance.sina.com.cn%2Fstock%2Fobserve%2F2025-02-08%2Fdoc-ineiumyy8905576.shtml" target="_blank">
	多氟多业绩大额预亏 早年埋下逆势扩产的雷终究还是炸了
</a></li>
						
```



### selenium

如果只用 Python 的 requests 库进行请求，可能得到原始页面会发现没有任何内容，原因在于网站是通过网页的 JavaScript 脚本进行即时渲染的，只有通过浏览器访问执行了 JS 脚本后才会显示出所有链接，而 request 库直接请求的页面原内容并没有执行 JS 脚本。因此，需要利用 selenium 模拟浏览器访问这个页面来爬取。

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

DRIVER_PATH = "./chromedriver"


def get_driver():
    if not os.path.exists(DRIVER_PATH):
        driver_path = ChromeDriverManager().install()
        shutil.copy(driver_path, DRIVER_PATH)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-blink-features=AutomationControlled")

    return webdriver.Chrome(service=Service(DRIVER_PATH), options=options)


driver = get_driver()
```

得到 `driver` 对象后即可进行爬取：

```python
root_url = "https://news.sina.com.cn/roll/"
driver.get(root_url)
driver.implicitly_wait(5)
content = driver.page_source
```



## 筛选内容

### 正则表达式

观察爬取到的网页的一部分：

```
https://finance.sina.com.cn/stock/marketresearch/2025-02-09/doc-ineivyah8211991.shtml
```

也就是说，要将内容中所有形如这个的链接，通过正则表达式将所有像这样的链接筛选出来

```python
# Get news list by regex
pattern = r"https://finance\.sina\.com\.cn/[a-zA-Z0-9/_-]+/doc-[a-zA-Z0-9]+\.shtml"
news_list = re.findall(pattern, content)
```

### BeautifulSoup 筛选

可以看到，所有的链接，都是包含在列表元素 li 下的超链接 a 元素，并且指向的链接是 a 元素的 href 属性，那么就通过 BS 筛选出所有 li下的 a 并获取其属性即可：

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(content, 'html.parser')

links = soup.select('li>a')
news_list = []
for link in links:
    news_list.append(link.get('href'))
    
# news_list = [link.get('href') for link in soup.select('li > a') if link.get('href')]
```



## 进一步操作

通过上面请求页面并获取网页原内容，并筛选出所需要的信息，基本上已经完成了爬虫的基本功能，接下来的操作思路基本一样。

### 解析新闻页面

获取了新闻链接后，再逐一访问单独的新闻页面以获取所需要的内容，存入一个字典中，如果需要可以将其存入本地数据库中。

```python
def get_news_content_from_url(url):
    """
    Get news content from html content
    Record url, title, time and article
    :param url
    :return: news content_dict
    """
    news_dict = {'url': url}

    driver.get(url)
    content = driver.page_source

    soup = BeautifulSoup(content, 'lxml')
    news_title = soup.select('h1.main-title')[0].text.strip()
    news_dict['title'] = news_title

    news_time_temp = datetime.datetime.strptime(
        soup.select('span.date')[0].text.strip(),
        '%Y年%m月%d日 %H:%M'
    )

    news_time = (news_time_temp

                 .strftime('%Y-%m-%d %H:%M:%S'))
    news_dict['time'] = news_time

    news_article = soup.select('div#artibody p')

    news_article_text = ''
    for paragraph in news_article:
        news_article_text += paragraph.text.strip()
    news_dict['article_text'] = news_article_text

    return news_dict
```

### 存入数据库

这里使用 SQLite 作为数据库，在存入之前，首先要创建数据库和数据表：

```python
def create_table():
    """
    Create a news database while initializing
    :return:
    """
    conn = sqlite3.connect('news_data.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS news (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT,
        published_time TEXT,
        url TEXT UNIQUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    conn.commit()
    conn.close()
    print("Database and table created successfully!")
```

然后可以将获取的新闻的字典存入数据库中，其中字典的 url 作为键值，检查并避免重复。

```python
def save_news_to_db(news_dict):
    """
    Check for duplicate URLs before inserting into the database
    """
    conn = sqlite3.connect('news_data.db')
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM news WHERE url = ?', (news_dict['url'],))
    exists = cursor.fetchone()[0]

    if exists:
        print(f"Duplicate URL, skipped: {news_dict['title']}")
    else:
        cursor.execute('''
        INSERT INTO news (title, content, published_time, url)
        VALUES (?, ?, ?, ?)
        ''', (
            news_dict['title'],
            news_dict['article_text'],
            news_dict['time'],
            news_dict['url']
        ))
        conn.commit()
        print(f"Saved to DB: {news_dict['title']}")

    conn.close()
```

