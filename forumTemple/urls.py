"""
URL configuration for forumTemple project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path

from index.views import index as index
from index.views import info as info
from index.views import info_0 as info_0

from admin_page.views import index as admin_index
from admin_page.views import action as admin_action

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', index, name='index'),
                  path('account/', admin_index, name='admin_index'),
                  path('account/action', admin_action, name='admin_action'),
                  path('info/', info_0),
                  path('info/<str:id>', info, name="info"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
