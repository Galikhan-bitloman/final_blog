from rest_framework import serializers

from .models import Post, Task

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields =['id', 'author', 'title', 'body', 'updated', 'created']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'completed']

