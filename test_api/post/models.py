from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey('core.User', related_name='author')

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title