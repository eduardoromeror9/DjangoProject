from django.contrib import admin
from .models import Page

# Register your models here.
admin.site.register(Page)

# Configuracion del Panel

title = 'Project ADMIN'
subtitle = 'Management Panel'

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle