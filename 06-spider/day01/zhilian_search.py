
import urllib.request
from urllib import parse


def get_zhilian_html(url):

    header = {
        'User-Agent': ''
    }
    

def main():

    city = input('搜索的城市：')
    job = input('搜索的岗位：')
    search = parse.urlencode({'jl':city, 'kw': job})
    url = 'https://'
    get_zhilian_html()


if __name__ == '__main__':
    main()