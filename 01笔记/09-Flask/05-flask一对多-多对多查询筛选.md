flask查询筛选

![52887422908](assets/1528874229087.png)



### 一对多查询

定义模型

-   ==1==的一方

建立 `students = dbrelationship('Studnet', backref='grade', lazy=True)`

其中   Student 是对应 一对多关系中的 ==多==的一方的==model==名称, 

#### backref   自定义的值, 用来查询, 一般写 model 名称 方便阅读

-   一对多关系中==多==的一方需要查询时使用, 通过backref可以查到对应的 ==一==的一方的model, 而通过多的一方的


many

-   `grades = db.Column(db.Integer, db.ForeignKey('tb_grade.g_id'), nullable=True)`


```python
many.backref   # 得到对应的 one 的一方的 models

many.关联的many的字段,  得到的是 db.ForeignKey() 中定义的表中的字段的值

one.多的一方的关联字段(backref不显示的字段)  得到 当前 one 下所有的的  many

```





### Django

 models  `relation_name`关联查询



pycharm继承git



### 多对多查询

关联关系  `relationship` 可以写在任意一方,相对于一对多关系, 增加一个`secondary=中间表`

中间表

-   将多对多的两张表的主键作为其外键关联, 并且将对应的两个字段都设置为主键

```python
sc = db.Table('tb_sc',  # 数据库表名
              db.Column('s_id', db.Integer(16), db.ForgignKey('tb_student.s_id'), primaryKey=True)
              db.Column('c_id', db.Integer(16), db.ForeignKey('tb_course.c_id'), primaryKey=True)
             )
```



### 登录 注册



`os.urandom(n)`   生成随机数, 可以用作加密的密匙使用

