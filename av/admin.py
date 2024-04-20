from django.contrib import admin
from av.models import Brand

# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name', 'slug')
    list_editable = ('name', 'slug')
    list_filter = ('name', 'slug')


admin.site.register(Brand, BrandAdmin)
