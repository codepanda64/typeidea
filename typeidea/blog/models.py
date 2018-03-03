from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    STATUS_ITEMS = (
        (1, '上线'),
        (2, '草稿'),
        (3, '删除'),
    )
    title = models.CharField(max_length=50, verbose_name="标题")
    desc = models.CharField(max_length=255, blank=True, verbose_name="摘要")
    category = models.ForeignKey("Category", on_delete=False, verbose_name="分类")
    tag = models.ManyToManyField('Tag', verbose_name="分类")
    content = models.TextField(verbose_name="内容",
                                help_text="注:目前仅支持Markdown数据格式")
    status = models.IntegerField(default=1, choices=STATUS_ITEMS, verbose_name="状态")
    owner = models.ForeignKey(User, on_delete=False, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name



class Category(models.Model):
    STATUS_ITEMS = (
        (1, '可用'),
        (2, '删除'),
    )
    name = models.CharField(max_length=50, verbose_name="名称")
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name="状态")
    is_nav = models.BooleanField(default=False, verbose_name="是否为导航")
    owner = models.ForeignKey(User, on_delete=False, verbose_name="作者")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name


class Tag(models.Model):
    STATUS_ITEMS = (
        (1, '正常'),
        (2, '删除'),
    )
    name = models.CharField(max_length=10, verbose_name="名称")
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name="状态")
    owner = models.ForeignKey(User, on_delete=False, verbose_name="作者")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name