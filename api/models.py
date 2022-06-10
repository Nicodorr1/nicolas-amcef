from django.db import models

# Create your models here.


class Post(models.Model):
    userId = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.title

    def snippetPost(self):
        return self.body[:50] + " ..."

