from rest_framework import serializers
from demo01 import models




#我们可以存 进数据库


#类名固定为表名 + Serializer   自定义方法，自定义
class PublisherSerializer(serializers.ModelSerializer):
    #read_only必须为True,因为我们模型里面的id是一个自增字段，不可写，自动生成
    #read_only=True 是只读的意思
    # operator = serializers.ReadOnlyField(source='operator.username')
    class Meta:#元信息

        model = models.Publisher  #要（或者说反序列化）序列化
        # fields = (
        #     'id',
        #     'title',
        #     'address'
        # )
        fields = "__all__"


class BookSerializers(serializers.HyperlinkedModelSerializer):
    """图书的序列化类"""
    # publisher = serializers.StringRelatedField(source='publisher.title')
    class Meta:
        model = models.Book
        fields = (
            'id',
            'title',
            'publisher'
        )