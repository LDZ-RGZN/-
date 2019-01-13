from rest_framework import serializers
from data_01 import models
class zongleiSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.zonglei
        fields = (
            'id',
            'category',
            'CGurl',
        )

class liebiaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.liebiao
        fields = (
            'id',
            'bookname',
            'author',
            'category',
            'State',
            'WordNumber',
            'introduce',
        )
class zhangjieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.zhangjie
        fields = (
            'id',
            'name',
            'zj_link',
            'mf',
        )
class contentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.content
        fields = (
            'id',
            'title',
            'bookname',
            'author',
            'WordNumber',
            'FaBuData',
            'content',
        )
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserInfo
        fields = (
            'id',
            'user_type',
            'user',
            'pwd',
        )