from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    date_published = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.author.username} Post'

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     self.image.delete()
    #     super().save(*args, **kwargs)

    # def __unicode__(self):
    #     return self.title
