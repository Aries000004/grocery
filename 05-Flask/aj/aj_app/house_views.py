import os

from flask import Blueprint, render_template, url_for, \
    request, session, jsonify

from aj_app.models import Area, House, HouseImage, \
    Facility, Order, db
from utils import status_code
from utils.decorator import login_required


house_blueprint = Blueprint('house', __name__)

# @house_blueprint.route('/drop_all/')
# def drop():
#     db.drop_all()
#     return 'drop_all'
#
#
# @house_blueprint.route('/create_all/')
# def create():
#     db.create_all()
#     return 'create_all'


@house_blueprint.route('/', methods=['GET'])
def index():

    return render_template('index.html')


@house_blueprint.route('/myhouse/', methods=['GET'])
@login_required
def my_house():
    """我的房源页面  GET"""
    return render_template('myhouse.html')


@house_blueprint.route('/all_houses/', methods=['GET'])
@login_required
def all_houses():

    user_id = session['user_id']
    all_houses = House.query.filter(House.user_id==user_id).all()
    houses = [house.to_dict() for house in all_houses]

    return jsonify(code=status_code.OK, houses=houses)


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


@house_blueprint.route('/newhouse/', methods=['POST'])
def user_new_house():
    """发布新房源"""
    data = request.form.to_dict()  # 得到的是表单的字典
    facilities = request.form.getlist('facility')
    house = House()

    house.user_id = session['user_id']
    house.title = data.get('title')
    house.price = data.get('price')
    house.area_id = data.get('area_id')
    house.address = data.get('address')
    house.room_count = data.get('room_count')
    house.acreage = data.get('acreage')
    house.unit = data.get('unit')
    house.capacity = data.get('capacity')
    house.beds = data.get('beds')
    house.deposit = data.get('deposit')
    house.min_days = data.get('min_days')
    house.max_days = data.get('max_days')

    facilities_list = Facility.query.filter(Facility.id.in_(facilities)).all()
    house.facilities = facilities_list
    try:
        house.add_update()
    except Exception as e:
        db.session.rollback()
        return jsonify(status_code.DATABASE_ERROR)

    return jsonify(code=status_code.OK, house_id=house.id)


@house_blueprint.route('/house_image/', methods=['POST'])
def house_image():
    """添加房屋的图片"""
    house_id = request.form.get('house_id')
    hosue_image = request.files.get('house_image')

    save_url = os.path.join('/static/uoload/', house_image.filename)
    house_image.save(save_url)

    image_url = os.path.join('upload', house_image.filename)

    # 保存房屋首图
    house = House.query.get(house_id)
    if not house.index_image_url:
        house.index_image_url = image_url
        house.add_update()

    h_image = HouseImage()
    h_image.house_id = house_id
    h_image.url = image_url

    h_image.add_update()

    return jsonify(status_code.SUCCESS)


@house_blueprint.route('/detail/', methods=['GET'])
def detail():
    """房屋的详细信息页面"""
    return render_template('detail.html')


@house_blueprint.route('/detail/<int:id>/', methods=['GET'])
def house_detail(id):

    house = House.query.get(id)
    house_info = house.to_full_dict()

    # facility_list = house.facilities
    # facility_info = [facility.to_dict() for facility in facility_list]

    return jsonify(code=status_code.SUCCESS,
                   house_info=house_info)


@house_blueprint.route('/booking/', methods=['GET'])
def booking():

    return render_template('booking.html')


