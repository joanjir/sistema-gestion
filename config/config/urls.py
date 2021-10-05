
from django.contrib import admin
from django.urls import path, include
#from login.views import *

from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sgfeufac2/', include('core.misitio.urls')),


]
