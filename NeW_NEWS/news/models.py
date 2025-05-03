from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='article_images/', blank=True, null=True)

    def __str__(self):
        return str(self.title)


