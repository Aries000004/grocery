""" 状态码 """

OK = 200  # 请求成功

# 用户模块
USER_REGISTER_DATA_NOT_NULL = {'code': 1004, 'msg': '该用户已注册,请直接登录'}
USER_REGISTER_PHONE_NOT_VALID = {'code': 1002, 'msg': '手机号码不正确'}
USER_REGISTER_PASSWORD_ERROR = {'code': 1003, 'msg': '密码错误'}
USER_REGISTER_PHONE_ALERDY_EXISTS= {'code': 1004, 'msg': '该用户已注册,请直接登录'}
USER_REGISTER_SUCCESS = { 'code': OK, 'msg': '注册成功!'}

# login
USER_LOGIN_USER_NOT_EXISTS = {'code': 1005, 'msg': '该用户不存在, 请先注册'}
USER_LOGIN_PASSWORD_ID_NOT_VALID = {'code': 1006, 'msg': '密码输入错误'}
USER_LOGIN_SECCESS = {'code': OK, 'msg': '登录成功!'}

# 上传文件
USER_PROFILE_ERROR = {'code': 1007, 'msg': '文件格式不正确'}
DATABASE_ERROR = {'code': 1008, 'msg': '数据库错误, 请稍后再试'}

USER_INFO_NAME_CHANGE = {'code': 1009, 'msg': '用户名更换成功'}


