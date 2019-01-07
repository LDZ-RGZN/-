from django.shortcuts import render

from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view



from app01 import serializers
from app01.models import *
from app01.permissions import IsOwnerOrReadOnly
#TODO 起始页的API
@api_view(['GET'])
def api_root(request, format=None):
    return Response(
        {
            '省份': reverse('shengfen-list', request=request, format=format),
            '详情地址': reverse('xqdz-list', request=request, format=format),
            '店铺名称': reverse('dianpu-list', request=request, format=format),
            '经营资金': reverse('dpmoney-list', request=request, format=format),
            '经营项目': reverse('dpproject-list', request=request, format=format),
        }
    )

class ShengFenViewSet(viewsets.ModelViewSet):
    """省份"""
    queryset = ShengFen.objects.all()
    serializer_class = serializers.ShengFenSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class XqDzViewSet(viewsets.ModelViewSet):
    """详情地址"""
    queryset = XqDz.objects.all()
    serializer_class = serializers.XqDzSerializer

class DianPuViewSet(viewsets.ModelViewSet):
    """店铺"""
    queryset = DianPu.objects.all()
    serializer_class = serializers.DianPuSerializer

class DpMoneyViewSet(viewsets.ModelViewSet):
    """资金"""
    queryset = Dp_money.objects.all()
    serializer_class = serializers.Dp_moneySerializer

class DpPorjectViewSet(viewsets.ModelViewSet):
    """项目"""
    queryset = Dp_project.objects.all()
    serializer_class = serializers.Dp_projectSerializer