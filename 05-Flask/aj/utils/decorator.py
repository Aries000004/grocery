from flask import redirect, url_for, session


def login_required(func):
    def check_logon():
            user_id = session.get('user_id')
            if user_id:
                return func()
            else:
                return redirect(url_for('user.login'))
    return check_logon