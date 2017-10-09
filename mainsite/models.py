from django.db import models
from django.utils import timezone

# Create your models here.

class Tag(models.Model):
    name = models.CharField('标签名', max_length=63)

    def __str__(self):
        return self.name

class Post(models.Model):
    """
        文章
    """

    title = models.CharField(max_length=127, verbose_name='标题')
    slug = models.SlugField('链接名', max_length=127, unique=True)
    body = models.TextField('正文')
    pub_date = models.DateTimeField(auto_now_add=True)
    illustration = models.CharField('配图', max_length=255)
    tags = models.ManyToManyField(Tag)
    summary = models.TextField('摘要')
    isTech = models.BooleanField(default=False)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title

class Pastime(models.Model):
    """
        阅读
    """

    CATEGORYS = (
        ('M', 'Movie'),
        ('B', 'Book'),
        ('G', 'Game'),
        ('A', 'Animation'),
        ('O', 'Other')
    )
    illustration = models.CharField('配图', max_length=255)
    name = models.CharField('标题', max_length=31)
    category = models.CharField('类别', max_length=1, choices=CATEGORYS)
    finTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-finTime',)
