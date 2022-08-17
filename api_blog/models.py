from django.db import models


class Post(models.Model):
    author = models.ForeignKey('auth.User', max_length=100, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Title')
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(verbose_name='Completed')

    def __str__(self):
        return self.title
