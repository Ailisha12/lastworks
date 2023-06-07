from django.contrib import admin

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Medallion)
admin.site.register(Earrings)
admin.site.register(Ring)
admin.site.register(Category, CategoryAdmin)
