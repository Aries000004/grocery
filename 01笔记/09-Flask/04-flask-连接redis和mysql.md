models 和连接数据库



#### 简介

Flask默认并没有提供任何数据库操作的API

我们可以选择任何适合自己项目的数据库来使用

Flask中可以自己的选择数据，用原生语句实现功能，也可以选择ORM（SQLAlchemy，MongoEngine）

SQLAlchemy是一个很强大的关系型数据库框架，支持多种数据库后台。SQLAlchemy提供了高层ORM，也提供了使用数据库原生SQL的低层功能。

ORM：

```
将对对象的操作转换为原生SQL
优点
	易用性，可以有效减少重复SQL
	性能损耗少
	设计灵活，可以轻松实现复杂查询
	移植性好
```

针对于Flask的支持, 更多[官网地址](http://flask-sqlalchemy.pocoo.org/2.3/)



### redis

-   redis主要用来存储 ==session==

functions.py-> create_app()

redis配置

```python
  # 设置 密钥  数据库  redis
    app.config['SECRET_KEY'] = 'secret_key'
    app.config['SESSION_TYPE'] = 'redis'  # 选择数据库类型, 默认连接本地 redis

    # 连接指定的地址, 连接本地, 设置数据库的 地址, 默认的可以不写
    app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1',
                                              port=6379)
     # 添加 sessionid的前缀
    app.config['SESSION_KEY_PREFIX'] = 'flask'
    
      Session(app=app)
```





连接数据库[官网配置参数](http://www.pythondoc.com/flask-sqlalchemy/config.html)

### mysql

-   配置连接mysql
-   flask_sqlalchemy
-   配置数据库mysql

```python
 # 配置数据库
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/hello_flask'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app=app)
```

例：
访问mysql数据库，驱动为pymysql，用户为root，密码为123456，数据库的地址为本地，端口为3306，数据库名称HelloFlask

设置如下： "mysql+pymysql://root:123456@localhost:3306/HelloFlask"

在初始化__init__.py文件中如下配置：

```
app.config['SQLALCHEMY_TRAKE_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost:3306/HelloFlask"
```



### models

使用SQLALchemy的对象去创建字段

其中__==tablename==__指定创建的数据库的名称

```
创建models.py文件，其中定义模型

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):

    s_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(16), unique=True)
    s_age = db.Column(db.Integer, default=1)

    __tablename__ = "tb_student"
```

其中：

Integer表示创建的s_id字段的类型为整形，

primary_key表示是否为主键

String表示该字段为字符串

unique表示该字段唯一

default表示默认值

autoincrement表示是否自增



#### 创建数据库表

在视图函数中我们引入models.py中定义的db

-    db.create_all()表示创建定义模型中对应到数据库中的表


-   db.drop_all()表示删除数据库中的所有的表

```python
from App.models import db

@blue.route("/createdb/")
def create_db():
    db.create_all()
    return "创建成功"

@blue.route('/dropdb/')
def drop_db():
    db.drop_all()
    return '删除成功'
```



####初始化SQLAlchemy

```python
# 方法1
from flask-sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app=app)

# 方法2
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    db.init_app(app=app)
    return app

```

