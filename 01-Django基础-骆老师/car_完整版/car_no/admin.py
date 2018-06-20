from django.contrib import admin

# Register your models here.


from car_no.models import Car


class CarAdmin(admin.ModelAdmin):

    list_display = ('id', 'carno', 'case', 'cardate', 'punish', 'handing')
    ordering = ('id',)
    search_fields = ('carno',)


admin.site.register(Car, CarAdmin)