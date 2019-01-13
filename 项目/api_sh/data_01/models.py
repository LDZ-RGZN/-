from django.db import models

# Create your models here.

class zonglei(models.Model):
    category = models.CharField(max_length=100,verbose_name='类别')
    CGurl = models.TextField(verbose_name='类别链接')
    #操作者
    # operator = models.ForeignKey('auth.User')
    def __str__(self):
        return self.category
    class Meta:
        verbose_name = '总类别'
        verbose_name_plural = verbose_name


class liebiao(models.Model):
    bookname = models.CharField(max_length=200,verbose_name='书名')
    img_url = models.TextField(verbose_name='图片链接')
    author = models.CharField(max_length=100,verbose_name='作者')
    category = models.CharField(max_length=100,verbose_name='类别')
    State = models.CharField(max_length=100,verbose_name='状态')
    WordNumber = models.CharField(max_length=100,verbose_name='字数')
    introduce = models.TextField('简介')
    # 操作者
    # operator = models.ForeignKey('auth.User')
    def __str__(self):
        return self.bookname
    class Meta:
        verbose_name = '列表'
        verbose_name_plural = verbose_name

class zhangjie(models.Model):
    name = models.CharField(max_length=100,verbose_name='章节名称')
    zj_link = models.TextField(verbose_name='链接')
    mf = models.CharField(max_length=100,verbose_name='状态')
    # 操作者
    # operator = models.ForeignKey('auth.User')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name

class content(models.Model):
    title = models.CharField(max_length=100,verbose_name='章节名称')
    bookname = models.CharField(max_length=150,verbose_name='书名')
    author = models.CharField(max_length=100,verbose_name='作者')
    WordNumber = models.CharField(max_length=100,verbose_name='本章字数')
    FaBuData = models.CharField(max_length=200,verbose_name='发布时间')
    content = models.TextField('内容')
    # 操作者
    # operator = models.ForeignKey('auth.User')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '详情'
        verbose_name_plural = verbose_name

class UserInfo(models.Model):
    #用户类型
    type = (
        (1,'普通用户'),
        (2,'VIP'),
        (3,'SVIP'),
    )

    user_type = models.CharField(max_length=64,choices=type,verbose_name='用户类型')
    user = models.CharField(max_length=100,verbose_name='用户名')
    pwd = models.CharField(max_length=255,verbose_name='密码')
    def __str__(self):
        return self.user
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

