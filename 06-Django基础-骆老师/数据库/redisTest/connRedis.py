import redis


def main():
    client = redis.Redis(
        host='39.104.171.126',
        port='9000',
        password='qwertyuiop8'
    )
    client.get('*')

if __name__ == '__main__':
    main()