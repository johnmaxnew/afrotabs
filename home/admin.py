from django.contrib import admin

from home.models import Home, About, Contact, Privacy, Terms, Cookie

# Register your models here.
class HomeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    pass

admin.site.register(Home, HomeAdmin)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Privacy)
admin.site.register(Terms)
admin.site.register(Cookie)
