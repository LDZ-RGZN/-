from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from data_01.permissions import IsOwnerOrReadOnly

from data_01.models import *
from data_01.serializers import *

class zongleiViewSet(viewsets.ModelViewSet):
    """总分类"""
    queryset = zonglei.objects.all()
    serializer_class = zongleiSerializer
    # permission_classes = (IsOwnerOrReadOnly,)


class liebiaoViewSet(viewsets.ModelViewSet):
    """列表简介"""
    queryset = liebiao.objects.all()
    serializer_class = liebiaoSerializer
    # permission_classes = (IsOwnerOrReadOnly,)


class zhangjieViewSet(viewsets.ModelViewSet):
    """章节"""
    queryset = zhangjie.objects.all()
    serializer_class = zhangjieSerializer
    # permission_classes = (IsOwnerOrReadOnly,)


class contentViewSet(viewsets.ModelViewSet):
    """内容"""
    queryset = content.objects.all()
    serializer_class = contentSerializer
    # permission_classes = (IsOwnerOrReadOnly,)
#
class UserInfoViewSet(viewsets.ModelViewSet):
    """用户"""
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
