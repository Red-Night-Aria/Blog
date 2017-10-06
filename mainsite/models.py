from django.db import models
from django.utils import timezone

# Create your models here.

class Tag(models.Model):
    name = models.CharField('标签名', max_length=64)

    def __str__(self):
        return self.name

class Post(models.Model):
    """
        文章
    """

    title = models.CharField(max_length=128, verbose_name='标题')
    slug = models.SlugField('链接名', max_length=256, unique=True)
    body = models.TextField('正文')
    pub_date = models.DateTimeField(auto_now_add=True)
    illustration = models.CharField('配图', max_length=256, null=True)
    tags = models.ManyToManyField(Tag)
    summary = models.TextField('摘要', default="请输入摘要")
    isTech = models.BooleanField(default=False)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title

class Pastime(models.Model):
    """
        阅读
    """

    illustration = models.CharField('配图', max_length=256, null=True)
    name = models.CharField('标题', max_length=32)
    isFin = models.BooleanField('是否阅读完毕', default=False)
    finTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-finTime',)