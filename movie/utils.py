from rest_framework import serializers

def is_rating(value):
    if value < 1:
        raise serializers.ValidationError('Value cannot be lower than 1.')
    elif value > 10:
        raise serializers.ValidationError('Value cannot be higher than 10')
        raise serializers.ValidationError('Value cannot be higher than 10')

def multiple_of_ten(value):
    if value % 10 != 0:
        raise serializers.ValidationError('Not a multiple of ten')