
"""

使用自动化测试工具 selenium 和 BeautifulSoup 抓取 拉钩网的职位信息

"""


import time
import pymongo

from selenium import webdriver
from bs4 import BeautifulSoup


def get_html(url, keywords):

    page_html_list = []
    chromeDriver = 'D:/00venv/soft/chromedriver_win32/chromedriver.exe'
    browser = webdriver.Chrome(chromeDriver)
    browser.get(url)  # 获取页面首页
    time.sleep(3)

    browser.find_element_by_xpath('//*[@id="changeCityBox"]/ul/li[7]/a').click()
    time.sleep(2)
    search = browser.find_element_by_xpath('//*[@id="search_input"]')
    for keyword in keywords:
        search.send_keys(keyword)  # 将关键字加入到搜索中
        browser.find_element_by_xpath('//*[@id="search_button"]').click() # 点击搜索
        # 翻页 获取数据
        flag = True
        retry_time = 0
        page_num = 2  # 默认是第一页， 换下一页从 2 开始
        while flag:
            page_html = browser.page_source
            page_html_list.append(page_html)
            # 下一页
            try:
                next_page = browser.find_element_by_xpath('//*[@id="s_position_list"]/div[2]/div/span[@page="%s"]' % page_num)
                next_page.click()
                page_num += 1
            except:
                retry_time += 1
                print('第 %s 次拿取失败！' % retry_time)
                if retry_time > 3:
                    print('结束获取页面')
                    flag = False

        time.sleep(3)
    browser.quit() # 关闭浏览器
    return page_html_list


def main():

    mongo = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    db = mongo.spider

    url = 'https://www.lagou.com/'
    keywords = ['python']
    # keywords = ['python', '爬虫', '大数据']
    page_html_list = get_html(url, keywords)  # 获取所有的网页信息
    for page_html in page_html_list:
        page = BeautifulSoup(page_html, 'lxml')   # 初始化 bs 对象
        company_list = page.find_all('div', {'class', 'list_item_top'}) # 获取每页的公司列表
        for company in company_list:  # 遍历 获取需要的信息

            company_name = company.find("", {'class': "company_name"}).find('a').get_text()
            job = company.find('h3').get_text()
            salary = company.find('span', {'class': 'money'}).get_text()
            # 插入数据库
            db.lagou.insert({'公司：': company_name, '职位：': job, '工资：': salary})


if __name__ == '__main__':
    main()

