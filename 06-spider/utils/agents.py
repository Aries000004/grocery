
import random


def randomHeader():
    agents_list = [
        'Baiduspider',
        'Googlebot',
        'Bingbot',
        '360Spider',
        'Yisouspider',
        'Sogouspider',
        'Yahoo!  Slurp',
        r'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    ]
    agent = agents_list[random.randint(0, len(agents_list) - 1)]

    header = {
        'User-Agent': agent
    }

    return header