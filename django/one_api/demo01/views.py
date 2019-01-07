"""
from django.shortcuts import render
from demo01.models import Publisher
import json
# 不管是提供API给客户端 还是 返回模板
# 都是写在视图 MVT 设计思想 Views --->>接受师徒 返回响应
from demo01 import serializers
from django.shortcuts import render
from django.http import HttpResponse
from django.forms import model_to_dict  # 可以将模型转换成字典
# from django.core import serializers #django提供的序列化的类
# 本质生  可以将模型转json

# 导入drf响应  DRF这个框架继承至http
from rest_framework.response import Response
# 导入一个请求
from rest_framework.decorators import api_view
from rest_framework import status
"""
# 基于类的视图 响应 状态码
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# TODO 要想使用混合视图我们需要导入
from rest_framework import mixins
from rest_framework import generics

#TODO 框架提供的权限
# from rest_framework import permissions
from demo01.permissions import IsOwnerOrReadOnly
# 模型和序列化类
from demo01.models import Publisher,Book  # 模型类
from demo01.serializers import PublisherSerializer,BookSerializers  # 序列化类
# TODO API 模块
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view


#视图集
from rest_framework import viewsets


#浏览API
@api_view(['GET'])
def api_root(request, format=None):
    return Response(
        {
            'publishers': reverse('publisher-list', request=request, format=format),
            'books': reverse('book-list', request=request, format=format)
        }
    )

class PublisherViewSet(viewsets.ModelViewSet):
    """出版社"""
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class BookViewSet(viewsets.ModelViewSet):
    """图书"""
    queryset = Book.objects.all()
    serializer_class = BookSerializers













"""
#浏览API
@api_view(['GET'])
def api_root(request, format=None):
    return Response(
        {
            'publishers': reverse('publisher-list', request=request, format=format),
            'books': reverse('book-list', request=request, format=format)
        }
    )











class PublisherList(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    #只有认真过得用户有权限
    permission_classes = (IsOwnerOrReadOnly,)

class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers





class PublisherList(
                    mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    generics.GenericAPIView
                    ):
    queryset = Publisher.objects.all()  #告诉CBV数据源
    serializer_class = PublisherSerializer()  #告诉CBV这个序列化的类

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class PublisherDetail(
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        generics.GenericAPIView
                    ):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
"""

"""
class PublisherList(APIView):
    # get post
    def get(self, request):
        # 获取出版社信息
        queryset = Publisher.objects.all()
        # 序列化
        s = PublisherSerializer(queryset, many=True)
        # 返回数据给调用者
        return Response(s.data, status=status.HTTP_200_OK)

    def post(self, request):
        # 提交数据者  他需要吧数据带给后台  request.data
        s = PublisherSerializer(data=request.data)
        # 验证数据是否正确
        if s.is_valid():
            s.save()  # 保存数据到数据库
            return Response(s.data, status=status.HTTP_201_CREATED)
        else:
            return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)

#修改 删除 获取单个出版社信息API
class PublisherDetail(APIView):
    def get_object(self,pk): #用来获取出版社信息的函数
        try:
            p = Publisher.objects.get(id=pk)
            return p
        except Publisher.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,pk):
        #先取数据
        p = self.get_object(pk)
        s = PublisherSerializer(p)
        return Response(s.data,status=status.HTTP_200_OK)
    def PUT(self,request,pk):
        s = PublisherSerializer(data=request.data)
        #校验
        if s.is_valid():
            s.save()
            return Response(s.data,status=status.HTTP_200_OK)
        else:
            return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        #删除数据
        p = self.get_object(pk)
        p.delete()
        return Response(status=status.HTTP_200_OK)

"""

# 请求和响应 请求(客户端) GET POST
# 实际的例子 现在我要请求 什么？  展示所有出版社
"""
# @api_view 让我们的普通视图成为一个drf视图  被允许请求的方式
@api_view(['GET', 'POST'])
def publishers(request):
    # 可以判断前段传过来的请求
    if request.method == 'GET':
        queryset = Publisher.objects.all()
        # 序列化
        s = serializers.PublisherSerializer(queryset, many=True)
        # print(s)
        # 返回响应
        return Response(s.data)
    # 当用户想要新增资源
    if request.method == 'POST':
        # drf框架对 request.data

        s = serializers.PublisherSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

# 刚刚我们获取所有数据 和提交一个新的数据
# 新的需求 是 跟新 删除 获取一个 单个出版社

@api_view(['GET','PUT','DELETE'])
def publisher_detail(request, pk):
    try:
        p = Publisher.objects.get(pk=pk)
    except Publisher.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        s = serializers.PublisherSerializer(p)
        return Response(s.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        s = serializers.PublisherSerializer(p,data=request.data)
        if s.is_valid():
            s.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        p.delete()
        return Response(status=status.HTTP_200_OK)
"""

'''
@api_view(['GET'])
def publisher(request):
    # 返回一个列表，列表里装的对象
    # p_list = Publisher.objects.all()
    # s = serializers.serialize('json',p_list)
    # data = []
    # for p in p_list:
    #     d = {
    #         'title': p.title,
    #          'address': p.address
    #     }
    #     data.append(d)
    # #进行序列化 s就是一个js字符串
    # #目的，数据传输
    # s = json.dumps(data),
    if request.method == 'GET':
        queryset = Publisher.objects.all()


        #我们需要吧这个列表对象转换字典   many=True：多个

        s = serializers.PublisherSerializer(queryset,many=True)
        #TODO 待定


        # return HttpResponse(json.dumps(s.data),content_type='application/json')

        return Response(s.data)
'''
