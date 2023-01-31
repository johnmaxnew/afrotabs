
from django.contrib import admin
from .models import Tab, Category

class TabAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    pass

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    pass


admin.site.register(Tab, TabAdmin)
admin.site.register(Category, CategoryAdmin)






