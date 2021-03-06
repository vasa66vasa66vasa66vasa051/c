

from django.contrib import admin
#from django.urls import include, path
from django.conf.urls import include,url
from  .views import index as local_index
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('s/', include('SystemNotification.urls')),
#     path('', local_index,name="index"),
# ]
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^s/', include('SystemNotification.urls')),
    url(r'^$', local_index,name="index"),
]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)