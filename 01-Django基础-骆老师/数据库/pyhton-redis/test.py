import pymysql


def test():
    db_create_sql = "create database msg default charset utf8;"
    drop_table_sql = "drop table if exists tb_addrBook;"
    create_table_sql ="""create table tb_addrBook
                (
                pid int auto_increment,
                name varchar(20) not null,
                sex bit default 1,
                tel char(11) not null,
                addr varchar(30),
                primary key (pid)
                );"""

    insert_sql = """insert into tb_addrBook (name, sex, tel, addr) values
                    (%(name)s, %(sex)s, %(tel)s, %(addr)s)                
                  """, {'name': '张五', 'sex': '1', 'tel': '12345678901', 'addr': '四川成都'}

    slt_name_sql = """select * from tb_addrBook where name='张三'"""

    update_msg_sql = 'update tb_addrBook set tel="00000000000" where name=%(name)s', {'name': '李四'}

    sql = [db_create_sql, drop_table_sql, create_table_sql, insert_sql,
            slt_name_sql, update_msg_sql]

    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           passwd='123456',
                           db='msg',
                           charset='utf8',
                           autocommit=False)
    try:
        with conn.cursor() as cursor:
            # 0-建数据库  1-删除表,如果已经存在 2-创建表格 3-插入值 4-筛选 5-更新数据
            result = cursor.execute()
            print(result)
            # cursor.execute(sql[4])
            # result = cursor.fetchone()
            # print(result)
            conn.commit()
    # except:
    #     conn.rollback()
    finally:
        conn.close()


def main():
    test()


if __name__ == '__main__':
    main()