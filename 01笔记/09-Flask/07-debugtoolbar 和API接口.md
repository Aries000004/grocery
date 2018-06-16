debugtoolbar 和 restful风格的 Api 接口



文件不能循环引用



**debugtoolbar**

```python
from flask_debugtoolbar import DebugToolbarExtension

toolbar = DebugToolbarExtension()

app.debug = True

toolbar.init_app(app=app)
```

内置面板说明

| 名称         | 说明                                                         |
| ------------ | ------------------------------------------------------------ |
| Versions     | 显示已安装的Flask版本, 展开会显示所有已安装的包              |
| Time         | 处理请求所用的时间, 包含CPU时间的细分                        |
| HTTP Headers | 显示请求头的HTTP信息                                         |
| Request Vars | 显示Flask请求相关的变量的详细信息, 包含视图函数参数, Cookie, 会话变量以及GET和POST变量 |
| Config       | 应用程序中的app.config信息                                   |
| Templates    | 显示有关为此请求呈现的模板的信息以及提供的模板参数的值       |
| SQLAlchemy   | 显示当前请求运行期间的SQL查询                                |
| Logging      | 显示当前请求期间的日志消息                                   |
| Route List   | 显示 Flask URL 路由规则                                      |
| Profiler     | 报告当前请求的分析数据, 由于性能开销, 分析在默认情况下是禁用的, 单机复选标记打开或者关闭分析, 启用分析后, 刷新页面以通过分析重新运行 |



#### Flask-Restful

`pip install flask-restful`



-   通过继承`flask_restful.Resourse`来重写其中的`get post put patch delete`方法来实现
-   返回的数据 JSON 格式的字典
-   也可以通过正常的视图来`return jsonify({返回的数据})`来实现 API 接口

##### 简单的 restful

create_app()

```python
from flask_restful import Api

api = Api()

api.init_app(app=app)
```

views

```python
from flask_restful import Resource
from utils.ext_app import api


class CourseApi(Resource):

    def get(self):
        courses = Course.query.all()
        data = [course.to_dict() for course in courses]
        # 返回 Json 格式
        return {
            'code': 200,
            'msg': '请求成功',
            'data': data,
        }

    def post(self):
        c_id = request.form.get('c_id')
        c_name = request.form.get('c_name')
        course = Course(c_id, c_name)
        course.save()
        return {
            'code': 200,
            'msg': '创建成功',
            'data': {c_id: c_name}
        }

    def put(self, id):
        pass

    def patch(self, id):
        pass
    
    def delete(self, id)
    course = Course.query.get(id)
        db.session.delete(course)
        db.session.commit()
         return {
            'code': 200,
            'msg': '删除成功',
            'data': {course.c_id: course.c_name}
        }


api.add_resource(CourseApi, '/api/course/', '/api/course/<int:id>/')
# 第二个 url 是为了在尽心修改删除等操作时方便获取需要修改的对象, 也使 url 完全符合了 restful 风格
```









