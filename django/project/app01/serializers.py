from rest_framework import serializers
from app01.models import *

#省份序列化
class ShengFenSerializer(serializers.ModelSerializer):
    # operator = serializers.ReadOnlyField(source='operator.username')
    class Meta:
        model = ShengFen
        fields = (
            'id',
            'guo_jia',
            'sheng_fen',
            'operator'
        )

#详情地址序列化
class XqDzSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = XqDz
        fields = (
            'id',
            'address',
            'shengfen',
        )
#店铺名称序列化
class DianPuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DianPu
        fields = (
            'id',
            'name',
            'xqdz',
        )
#店铺经营资金序列化
class Dp_moneySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dp_money
        fields = (
            'id',
            'money',
            'dianpu',
        )
#店铺经营项目序列化
class Dp_projectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dp_project
        fields = (
            'id',
            'project',
            'dp_money',
        )
