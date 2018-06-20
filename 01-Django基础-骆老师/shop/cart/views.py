from django.shortcuts import render, redirect

from cart.models import Goods


def index(request):
    goods_list = list(Goods.objects.all())
    return render(request, 'goods.html', {'goods_list': goods_list})


class CartItem(object):
    """
    购物车的商品项

    购物车的商品
    """

    def __init__(self, no,  goods, amount=1):
        self.no = no
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
        self.num = 1
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
    cart = request.session.get('cart', ShoppingCart()) # 获取session中的cart 如果没有, 就创建一个
    cart.add_item(CartItem(cart.num, goods))
    cart.num += 1
    request.session['cart'] = cart
    return redirect('/')


def show_cart(request):
    """
    查看购物车

    :return:
    """
    cart = request.session.get('cart', None)
    cart_items = cart.items.values() if cart else []
    total = cart.total if cart else 0
    return render(request, 'cart.html',
                  {'cart_items':cart_items, 'total': total})
