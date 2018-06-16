import pymysql


class Foo(object):
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           passwd='123456',
                           db='msg',
                           charset='utf8',
                           autocommit=False)
    cursor = conn.cursor()

    def __init__(self):
        pass

    def insert(self):
        temp = True
        try:
            while temp:
                name = input('请输入姓名:')
                sex = input('性别:')
                if sex == '1':
                    sex = 1
                elif sex == '0':
                    sex = 0
                else:
                    print('输入有误, 重新输入!!')
                    return
                tel = input('电话号码:')
                addr = input('家庭住址:')
                with Foo.conn.cursor() as cursor:
                    b = cursor.execute("""insert into tb_addrBook (name, sex, tel, addr) 
                                            values(%s, %s, %s, %s)""",(name, sex, tel, addr))
                    print(b)
                    Foo.conn.commit()
                #temp = False
        except:
            Foo.conn.rollback()
        finally:
            Foo.conn.close()

    def update(self):
        print('输入您要更新的姓名!')
        name = input('姓名:')
        try:
            with Foo.conn.cursor() as cursor:
                b = cursor.execute('update tb_addrBook set tel="00000000000" where name=%s', (name, ))
                print(b)
                Foo.conn.commit()
        finally:
            Foo.conn.close()

    def delate(self):
        print('输入您要删除的姓名!')
        name = input('姓名:')
        try:
            with Foo.conn.cursor() as cursor:
                b = cursor.execute('delete from tb_addrBook where name=%s',(name))
                print(b)
                Foo.conn.commit()
        finally:
            Foo.conn.close()

    def select(self):
        print('输入您要查找的姓名!')
        name = input('姓名:')
        try:
            with Foo.conn.cursor() as cursor:
                cursor.execute('select * from tb_addrBook where name=%s', (name))
                b = cursor.fetchone()
                print(b)
                Foo.conn.commit()
        finally:
            Foo.conn.close()

    def __str__(self, ):
        try:
            with Foo.conn.cursor() as cursor:
                cursor.execute('select (pid, name, sex, tel, addr) from tb_addrBook where name=%s', (name))
                b = cursor.fetchone()
                print(b)
        finally:
            Foo.conn.close()
        print()



def main():
    a = Foo()
    #a.insert()
    #a.update()
    # a.delate()
    print(a)


if __name__ == '__main__':
    main()