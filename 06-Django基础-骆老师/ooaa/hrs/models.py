from django.db import models


class Dept(models.Model):

    no = models.IntegerField(primary_key=True, verbose_name='部门编号')
    name = models.CharField(max_length=20, verbose_name='部门名称')
    location = models.CharField(max_length=20, verbose_name='部门所在地')
    excelent = models.BooleanField(default=0, verbose_name='优秀部门')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_dept'


class Emp(models.Model):
    no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    job = models.CharField(max_length=10)
    mgr = models.IntegerField(null=True, blank=True, verbose_name='主管')
    sal = models.DecimalField(max_digits=7, decimal_places=2)
    comm = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    dept = models.ForeignKey(Dept, on_delete=models.PROTECT)
    def __str__(self):
        return Dept.name


    class Meta:
        db_table = 'tb_emp'