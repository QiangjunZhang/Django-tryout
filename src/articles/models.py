from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200, default='New article')
    # author = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    content = models.TextField()

    def __str__(self):
        return self.title
