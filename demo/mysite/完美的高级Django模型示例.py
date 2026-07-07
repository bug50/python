from django.db import models
from django.urls import reverse
 
# 自定义Manager方法
class HighRatingManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(rating=1)

# CHOICES选项
class Rating(models.IntegerChoices):
    VERYGOOD = 1, 'Very Good'
    GOOD = 2, 'Good'
    BAD = 3, 'Bad'

class Product(models.Model):
    # 数据表字段
    name = models.CharField('name', max_length=30)
    rating = models.IntegerField(max_length=1, choices=Rating.choices)
 
    # MANAGERS方法
    objects = models.Manager()
    high_rating_products =HighRatingManager()
 
    # META类选项
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
 
    # __str__方法
    def __str__(self):
        return self.name
 
    # 重写save方法
    def save(self, *args, **kwargs):
        do_something()
        super().save(*args, **kwargs) 
        do_something_else()
 
    # 定义单个对象绝对路径
    def get_absolute_url(self):
        return reverse('product_details', kwargs={'pk': self.id})
 
    # 其它自定义方法
    def do_something(self):
        print("Doing something with the product")