from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:   # 指定模型的复数形式,不指定会在admin中自动加s
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=CASCADE)   # Category的主键作为本模板的外键
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    website = models.URLField(blank=True)   # 设置了blank 但是没有设置null属性
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
