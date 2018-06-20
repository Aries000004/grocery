from django.db import models


class Goods(models.Model):

    id = models.AutoField(primary_key=True, db_column='gid', verbose_name='商品编号')
    name = models.CharField(max_length=50, db_column='gname', verbose_name='商品名称')
    price = models.DecimalField(max_digits=7, decimal_places=2, db_column='gprice', verbose_name='商品价格')
    image = models.CharField(max_length=50, db_column='gimage', verbose_name='商品图片')

    class Meta:

        db_table = 'tb_goods'
        ordering = ('id',)

