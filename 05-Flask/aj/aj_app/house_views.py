
from flask import Blueprint, render_template, url_for, \
    request, session, jsonify

from aj_app.models import Area, House, HouseImage, Facility, Order
from utils import status_code
from utils.decorator import login_required


house_blueprint = Blueprint('house', __name__)


@house_blueprint.route('/myhouse/', methods=['GET'])
@login_required
def my_house():
    """我的房源页面  GET"""
    return render_template('myhouse.html')


@house_blueprint.route('/all_houses/', methods=['GET'])
@login_required
def all_houses():

    all_houses = House.query.all()

    return


@house_blueprint.route('/newhouse/', methods=['GET'])
def new_house():
    """添加新房源  GET"""
    return render_template('newhouse.html')


@house_blueprint.route('/area_facility/', methods=['GET'])
def area_facility():
    """ 地区信息 房屋设施信息 """
    all_areas = Area.query.all()
    all_facilities = Facility.query.all()

    areas = [area.to_dict() for area in all_areas]
    facilities = [facility.to_dict() for facility in all_facilities]
    resp = {
        'code': status_code.OK,
        'msg': '请求成功',
        'data': {
            'areas': areas,
            'facilities': facilities
        }
    }
    return jsonify(resp)