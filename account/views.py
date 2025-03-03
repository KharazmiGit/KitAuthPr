from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.decorators import login_required
from account.models import User
from account.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@login_required()
def auth_test(request):
    return render(request, 'index.html')
