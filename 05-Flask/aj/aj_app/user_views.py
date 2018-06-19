
import re
import os

from flask import Blueprint, render_template, \
    url_for, request, jsonify, session, redirect

from aj_app.models import db, User
from utils import status_code
from utils.decorator import login_required
from utils.settings import BASE_DIR, UPLOAD_DIR


user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/tb/')
def tb():
    db.create_all()
    return 'OK'


@user_blueprint.route('/register/', methods=['GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')


@user_blueprint.route('/register/', methods=['POST'])
def user_register():
    if request.method == 'POST':
        mobile = request.form.get('mobile')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        # 验证数据完整性
        if not all([mobile, password, password2]):
            return jsonify(status_code.USER_REGISTER_DATA_NOT_NULL)
        # 2. 验证手机号码是否真确
        if not re.match(r'^1[34578][0-9]{9}$', mobile):
            return jsonify(status_code.USER_REGISTER_PHONE_NOT_VALID)
        # 验证密码
        if not password == password2:
            return jsonify(status_code.USER_REGISTER_PASSWORD_ERROR)
        # 保存用户数据
        user = User.query.filter(User.phone==mobile).first()
        if user:
            return jsonify(status_code.USER_REGISTER_PHONE_ALERDY_EXISTS)
        else:
            user = User()
            user.phone = mobile
            user.name = mobile
            user.password = password
            user.add_update()
            return jsonify(status_code.USER_REGISTER_SUCCESS)


@user_blueprint.route('/login/', methods=['GET'])
def login():
    return render_template('login.html')


@user_blueprint.route('/login/', methods=['POST'])
def user_login():

    mobile = request.form.get('mobile')
    password = request.form.get('password')

    # 1.验证数据的完整性
    if not all([mobile, password]):
        return jsonify(status_code.USER_REGISTER_DATA_NOT_NULL)
    # 2. 验证手机正确性
    if not re.match(r'^1[34578][0-9]{9}$', mobile):
        return jsonify(status_code.USER_REGISTER_PHONE_NOT_VALID)
    # 3. 用户
    user = User.query.filter(User.phone == mobile).first()
    if user:
        if not user.check_password(password):
            return jsonify(status_code.USER_LOGIN_PASSWORD_ID_NOT_VALID)
        # 验证通过
        else:
            session['user_id'] = user.id
            return jsonify(status_code.USER_LOGIN_SECCESS)
    else:
        return jsonify(status_code.USER_LOGIN_USER_NOT_EXISTS)


@user_blueprint.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('user.login'))


@user_blueprint.route('/my/', methods=['GET'])
@login_required
def my():
    return render_template('my.html')


@user_blueprint.route('/user_info/', methods=['GET'])
def user_info():
    user_id = session.get('user_id')
    user = User.query.filter(User.id==user_id).first()
    if user:
        data = {
            'name': user.name,
            'phone': user.phone,
            'avatar': user.avatar.replace('\\', '/') if user.avatar else '',
        }
        return jsonify(data)


"""上传头像
"""


@user_blueprint.route('/profile/', methods=['GET'])
def profile():
    return render_template('profile.html')


@user_blueprint.route('/profile/', methods=['PATCH'])
def user_profile():

    file = request.files.get('avatar')
    name = request.form.get('name')
    if file:
        # 校验图片是否格式正确
        if not re.match(r'image/.*', file.mimetype):
            return jsonify(status_code.USER_PROFILE_ERROR) # 图片格式错误
        # 保存图片
        image_path = os.path.join(UPLOAD_DIR, file.filename)
        file.save(image_path)

        user = User.query.get(session['user_id'])
        avatar_path = os.path.join('upload', file.filename)
        user.avatar = avatar_path
        try:
            user.add_update()
        except Exception as e: # 数据库错误
            return jsonify(status_code.DATABASE_ERROR)
        # 上传成功, 将头像信息传回 渲染页面
        return jsonify(code=status_code.OK, img_url=avatar_path)
    # 更改姓名
    if name:
        user = User.query.get(session['user_id'])
        user.name = name
        user.add_update()
        return jsonify(status_code.USER_INFO_NAME_CHANGE)


