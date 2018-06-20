import redis


def main():
    client = redis.Redis(host='39.104.171.126', port='6379', password='qwertyuiop8')
    if client.ping():
        print(client.keys("*").decode('utf-8'))
        # print(client.get('username').decode('utf-8'))
        # print(client.get('name').decode('utf-8'))
        print(list(map(lambda x: x.decode('utf-8'),
                       client.zrange('foo', start=0, end=-1))))
        print([x.decode('utf-8')
               for x in client.zrange('foo', start=0, end=-1)])


if __name__ == '__main__':
    main()