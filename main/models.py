from django.db import models

class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to="news/img")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title