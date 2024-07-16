from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import UserSerializer


# создаем представление для работы с пользователями
class UserViewSet(viewsets.ViewSet):

    # получение списка пользователей
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    # получение информации о пользователе
    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    # создание нового пользователя
    def create(self, request):
        serializer = UserSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'User created': serializer.data})

    # обновление информации о пользователе
    def update(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        try:
            instance = User.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = UserSerializer(data=request.data, instance=instance, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'User updated': serializer.data})

    # удаление пользователя
    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})
        try:
            User.objects.filter(pk=pk).delete()
        except:
            return Response({"error": "Object does not exists"})

        return Response({"User deleted": str(pk)})
