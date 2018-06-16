from django.db import models

# Create your models here.
# 一个类对应一张表, 类的属性就是表的列, 创建的对象就对应着表里面的一条数据记录
# 对象关系映射   ORM
#

# 继承 models.Model


class Dept(models.Model):

    no = models.IntegerField(primary_key=True, verbose_name='部门编号')
    name = models.CharField(max_length=20, verbose_name='部门名称')  # 默认不为空 not null
    location = models.CharField(max_length=20, verbose_name='部门所在地')
    excelent = models.BooleanField(default=0, verbose_name='优秀部门')

    def __str__(self):
        return self.name

    class Meta:    # 添加内部类, 定义元数据
        db_table = 'tb_dept'     # 指定表名, 不使用默认的 hrs_dtpt


class Emp(models.Model):
    no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    job = models.CharField(max_length=10)
    mgr = models.IntegerField(null=True, blank=True, verbose_name='主管')   # null 数据库设置, blank 后台设置
    sal = models.DecimalField(max_digits=7, decimal_places=2)
    comm = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True) # null = True  表示可以放空值
    dept = models.ForeignKey(Dept, on_delete=models.PROTECT)   #放在 1对 多的 多的一方    在删除时保护  , null = True on_delete = models.setnull
    #  ForeignKey添加 related_name = '+' 防止反查

    def __str__(self):
        return Dept.name


    class Meta:
        db_table = 'tb_emp'