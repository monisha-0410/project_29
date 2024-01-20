from django.contrib import admin

# Register your models here.
from app.models import *

class WebPage_AdminView(admin.ModelAdmin):
    list_display=['Topic_name','name','url','Email']
    list_editable=('Email',)
    list_filter=['name']
    list_per_page=3
    list_display_links=['url']
    search_fields=['name','url']

admin.site.register(Topic)
admin.site.register(WebPage,WebPage_AdminView)
admin.site.register(AccessRecord)