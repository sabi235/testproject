from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


#Basic Serializers
# create a serializer
class UserBasicSerializer(serializers.Serializer):
    # initialize fields
    email = serializers.EmailField()
    username = serializers.CharField(max_length = 200)
    first_name = serializers.CharField(max_length = 200)
    last_name = serializers.CharField(max_length = 200)
    date_joined = serializers.DateTimeField()


#Model Serializers
class UserModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username', 'first_name', 'last_name', 'date_joined']


#Hyperlinked Serializers
class UserHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'url', 'username', 'first_name', 'last_name', 'date_joined']
