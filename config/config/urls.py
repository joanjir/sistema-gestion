
from django.contrib import admin
from django.urls import path, include
from core.login.views import *

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sgfeufac2.uci.cu/', include('core.misitio.urls')),
    path('login/', include('core.login.urls')),
    

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
