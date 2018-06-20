from django.contrib import admin

# Register your models here.
from dept.models import Dept, Emp


class DeptAdmin(admin.ModelAdmin):

    list_display = ('no', 'name', 'location')
    ordering = ('no',)  #元组 前面加 '-no' 为降序, 'no' 为升序


class EmpAdmin(admin.ModelAdmin):

    list_display = ('no', 'name', 'job', 'sal', 'comm', 'dept_id', 'mgr')
    search_fields = ('name',)
    ordering = ('dept_id',)


admin.site.register(Dept, DeptAdmin)
admin.site.register(Emp, EmpAdmin)

