from django.db import models

# Create your models here.


class Car(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='序号')
    carno = models.CharField(max_length=20, verbose_name='车牌号码')
    case = models.CharField(max_length=50, null=True, blank=True, verbose_name='违章理由')
    cardate = models.DateTimeField(default=0,null=True, blank=True, verbose_name='违章日期')
    punish = models.CharField(max_length=50, null=True, blank=True, verbose_name='处罚方式')
    handing = models.BooleanField(default=0, verbose_name='是否受理')

    @property
    def happen_date(self):
        return self.cardate.strftime('%Y-%m-%d %H:%M:%S')

    class Meta:
        db_table = 'tb_car'