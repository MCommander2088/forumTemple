# admin.py 中
from django.contrib import admin

admin.site.site_header = 'AQR Admin'  # 登录页标题
admin.site.site_title = 'AQR'  # 首页标题
admin.site.index_title = 'AQR'  # 网页标签标题

from .models import Level

admin.site.register(Level)
