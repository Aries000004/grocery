
from datetime import datetime

from flask import Blueprint, request, session, jsonify
from aj_app.models import db, House, Order

from utils import status_code

order_blueprint = Blueprint('order', __name__)


@order_blueprint.route('/create_order/', methods=['POST'])
def create_order():
    """创建一个订单"""
    # user_id = session['user_id']
    house_id = request.form.get('house_id')
    bg = datetime.strptime(request.form.get('bg'), '%Y-%m-%d')
    end = datetime.strptime(request.form.get('end'), '%Y-%m-%d')

    house = House.query.get(house_id)
    user = house.user

    days = (end - bg).days + 1
    if not days:
        return jsonify(status_code.ORDER_DAYS_ERROR)

    order = Order()
    order.user_id = user.id
    order.house_id = house_id
    order.begin_date = bg
    order.end_date = end
    order.days = days
    order.house_price = house.price
    order.amount = house.price * days

    order.add_update()

    return jsonify(status_code.SUCCESS)