
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class BaseModel(object):
    """基础模型"""
    create_time = db.Column(db.DATETIME, default=datetime.now())
    update_time = db.Column(db.DATETIME, default=datetime.now(),
                            onupdate=datetime.now())

    def add_update(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class User(BaseModel, db.Model):
    """用户模型"""
    __tablename__ = 'tb_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone = db.Column(db.String(11), unique=True)
    pwd_hash = db.Column(db.String(200))
    name = db.Column(db.String(30), unique=True)
    avatar = db.Column(db.String(30)) # 头像
    id_name = db.Column(db.String(30))  #  身份证姓名
    id_card = db.Column(db.String(18))  # 身份证号码

    @property
    def password(self):
        return "It's don't allow get directly"

    @password.setter
    def password(self, password):
        """生成密码"""
        self.pwd_hash = generate_password_hash(password)

    def check_password(self, password):
        """验证密码"""
        return check_password_hash(self.pwd_hash, password)

    def to_auth_dict(self):
        """序列化 身份信息"""
        return {
            'id_name': self.id_name,
            'id_card': self.id_card
        }

    def to_basic_dict(self):
        """序列化基础信息"""
        return {
            'id': self.id,
            'avatar': self.avatar if self.avatar else 'No avatar',
            'name': self.name,
            'phone': self.phone
        }
