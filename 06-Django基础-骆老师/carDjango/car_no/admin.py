
from django.contrib import admin

# Register your models here.


from car_no.models import Car


class CarAdmin(admin.ModelAdmin):

    list_display = ('id', 'no', 'case', 'date', 'punish', 'handing')
    ordering = ('id',)
    search_fields = ('no',)


admin.site.register(Car, CarAdmin)
# Register your models here.
