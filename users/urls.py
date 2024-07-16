from django.urls import path, include, re_path
from .views import UserViewSet
from rest_framework.routers import DefaultRouter

# создание роутера и регистрация эндпойнтов users для работы с пользователями
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    # подключение стандартных эндпойнтов авторизации drf
    path('auth', include('rest_framework.urls')),
    # подключение эндпойнтов библиотеки djoser
    path('auth-djoser', include('djoser.urls')),
    re_path(r'^auth-djoser/', include('djoser.urls.authtoken')),
]

urlpatterns += router.urls
