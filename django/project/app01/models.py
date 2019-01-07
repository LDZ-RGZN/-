from django.db import models

# Create your models here.

#省份表
class ShengFen(models.Model):
    guo_jia = models.CharField(max_length=50,verbose_name='国家')
    sheng_fen = models.CharField(max_length=100,verbose_name='省份')
    operator = models.ForeignKey('auth.User',verbose_name='操作者')

    def __str__(self):
        return self.sheng_fen
    class Meta:
        verbose_name = '省份'
        verbose_name_plural = verbose_name

#详情地址表
class XqDz(models.Model):
    address = models.CharField(max_length=200,verbose_name='详情地址')
    shengfen = models.ForeignKey('ShengFen',verbose_name='省份')
    operator = models.ForeignKey('auth.User',verbose_name='操作者')

    def __str__(self):
        return self.address
    class Meta:
        verbose_name = '详情地址'
        verbose_name_plural = verbose_name

#店铺表
class DianPu(models.Model):
    name = models.CharField(max_length=100,verbose_name='店铺名称')
    xqdz = models.ForeignKey('XqDz',verbose_name='详情地址')
    operator = models.ForeignKey('auth.User',verbose_name='操作者')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '店铺名称'
        verbose_name_plural = verbose_name

#店铺经营资金
class Dp_money(models.Model):
    money = models.CharField(max_length=100,verbose_name='经营资金')
    dianpu = models.ForeignKey('DianPu',verbose_name='店铺')
    operator = models.ForeignKey('auth.User',verbose_name='操作者')

    def __str__(self):
        return self.money
    class Meta:
        verbose_name = '经营资金'
        verbose_name_plural = verbose_name

#店铺经营项目
class Dp_project(models.Model):
    project = models.CharField(max_length=100,verbose_name='经营项目')
    dp_money = models.ForeignKey('Dp_money',verbose_name='资金')
    operator = models.ForeignKey('auth.User',verbose_name='操作者')

    def __str__(self):
        return self.project
    class Meta:
        verbose_name = '项目'
        verbose_name_plural = verbose_name