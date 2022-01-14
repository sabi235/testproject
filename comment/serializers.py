from rest_framework import serializers
from .models import Comment, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class CommentSerializer(serializers.ModelSerializer):
    # Explicit definition
    # author = UserSerializer()

    class Meta:
        model = Comment
        fields = '__all__'
    # Using the depth field
        depth = 2