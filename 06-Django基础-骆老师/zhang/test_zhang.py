import time


def timmer(func):
    def warpper(*args, **kwargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print('运行时间: %s' % (stop_time - start_time))
    return warpper()

@timmer
def test1():
    time.sleep(2)
    print("in the test1")