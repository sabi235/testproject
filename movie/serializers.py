from django.db.models import IntegerField
from rest_framework import serializers
from .models import Movie
from .utils import is_rating


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        # rating = IntegerField(validators=[multiple_of_ten])

    # custom field validation
    def validate_rating(self, value):
        if value < 10 or value > 20:
            raise serializers.ValidationError('Rating has to be between 10 and 20.')
        return value

    # object level validation
    def validate(self, data):
        if data['us_gross'] > data['worldwide_gross']:
            raise serializers.ValidationError('worldwide_gross cannot be bigger than us_gross')
        return data

    # functional validators
    def is_rating(value):
        if value < 1:
            raise serializers.ValidationError('Value cannot be lower than 1.')
        elif value > 10:
            raise serializers.ValidationError('Value cannot be higher than 10')
            raise serializers.ValidationError('Value cannot be higher than 10')