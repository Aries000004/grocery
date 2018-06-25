
import re

import urllib.request
from urllib import parse


def get_zhilian_html(url, search):
    url = url + search
    header = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    req = urllib.request.Request(url=url, headers=header)
    res = urllib.request.urlopen(req)

    return res.read().decode('utf-8')


def get_job_num(html):
    num = re.
    return


def main():

    city = input('搜索的城市：')
    job = input('搜索的岗位：')
    search = parse.urlencode({'jl':city, 'kw': job})
    url = 'https://'
    html = get_zhilian_html(url, search)



if __name__ == '__main__':
    main()