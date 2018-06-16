from django.contrib import admin

# Register your models here.
from hrs.models import Dept


class DeptAdmin(admin.ModelAdmin):

    list_display = ('no', 'name', 'location')
    ordering = ('no',)


admin.site.register(Dept, DeptAdmin)

