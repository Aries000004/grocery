from datetime import datetime
from json import dumps

from django.http import HttpResponse
from django.shortcuts import render, redirect

from cart.models import Goods


def index(request):
    goods_list = list(Goods.objects.all())
    return render(request, 'shopping/goods.html', {'goods_list': goods_list})


class CartItem(object):
    """
    购物车的商品项

    购物车的商品
    """

    def __init__(self,  goods, amount=1):
        self.goods = goods
        self.amount = amount

    @property
    def total(self):
        """
        小计

        :return: 商品的总价
        """
        return self.goods.price * self.amount


class ShoppingCart(object):
    """购物车"""

    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item.goods.id in self.items:
            self.items[item.goods.id].amount += item.amount
        else:
            self.items[item.goods.id] = item

    def remove_item(self, id):
        if id in self.items:
            self.items.remove(id)

    def clear_all_items(self):
        """
        清空

        """
        self.items.clear()

    @property
    def total(self):
        val = 0
        for item in self.items.values():
            val += item.total
        return val


def add_to_cart(request, id):
    """
    加商品到购物车

    :param id:
    :return:
    """
    goods = Goods.objects.get(pk=id)
    cart = request.session.get('cart') # 获取session中的cart 如果没有, 就创建一个
    if not cart:
        cart = ShoppingCart()
    print(cart)
    item = CartItem(goods)
    cart.add_item(item)
    request.session['cart'] = cart
    return redirect('/cart/')


def show_cart(request):
    """
    查看购物车

    :return:
    """
    current_time = datetime.now().ctime()
    last_vist_time = request.COOKIES.get('last_vist_time', '第一次访问')

    cart = request.session.get('cart', None)
    cart_items = cart.items.values() if cart else []
    total = cart.total if cart else 0
    ctx = {
        'cart_items': cart_items,
        'total': total,
        'last_vist_time': last_vist_time
    }
    response = render(request, 'shopping/cart.html', ctx)
    response.set_cookie('last_vist_time', current_time)
    return response


def clear_cart(request):
    cart = request.session['cart']
    cart.clear_all_items()
    request.session['cart'] = cart
    if not cart.items:
        ctx = {'code': 200}
    render(request, 'shopping/cart.html')
    json_str = dumps(ctx)
    return HttpResponse(json_str, content_type='application/json; charset=utf-8;')

