from django.contrib import admin

from rango.models import Category, Page, UserProfile


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

    class Meta:
        model = Page
        exclude = ('category',)
        #fields = ('title', 'url', 'views')    # 只显示包含的字段
    


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = Category
        fields = ('name', 'views', 'likes', 'slug')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)

