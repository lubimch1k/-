from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=32)

    def __str__(self):
        return str(self.category_name)



class Product(models.Model):
    product_name = models.CharField(max_length=128)
    product_des = models.TextField()
    product_count = models.IntegerField()
    product_price = models.FloatField()
    product_photo = models.ImageField(upload_to='media')
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.product_name)


class Cart(models.Model):
    user_id = models.ImageField()
    user_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_pr_count = models.IntegerField()

    def __str__(self):
        return str(self.user_id)

class NewsCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return str(self.name)

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Основной текст')
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, related_name='news', verbose_name='Категория')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return str(self.title)