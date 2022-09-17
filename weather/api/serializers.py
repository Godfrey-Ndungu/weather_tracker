from rest_framework import serializers

class WeatherSerializer(serializers.Serializer):
    maximum = serializers.IntegerField()
    minimum = serializers.IntegerField()
    avarage = serializers.IntegerField()
    median = serializers.IntegerField()
