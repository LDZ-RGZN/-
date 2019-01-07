from django.db import models


#写我们的模型类
#ORM 模型类就相当于数据库里面的一张表
class Publisher(models.Model):
    # id = models.AutoField()
    title = models.CharField(max_length=100,verbose_name='标题')
    address = models.CharField(max_length=200,verbose_name='地址')
    #操作者
    operator = models.ForeignKey('auth.User')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '出版社'
        verbose_name_plural = verbose_name
class Book(models.Model):
    '''书'''
    title = models.CharField(max_length=32,verbose_name='书名')
    publisher = models.ForeignKey('Publisher')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '书'
        verbose_name_plural = verbose_name


