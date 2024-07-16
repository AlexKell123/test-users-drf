from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # подключение админ-панели
    path('admin/', admin.site.urls),
    # подключение файла users.urls
    path('users/', include('users.urls')),
]
