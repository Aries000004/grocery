

class foo():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def fuc(self):
        print('hello')

    def __str__(self):
        return self.a + self.b


a = foo('aaa', 'bbb')
# a.fuc()
print(a)