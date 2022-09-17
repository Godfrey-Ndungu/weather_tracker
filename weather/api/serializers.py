from rest_framework import serializers

class WeatherSerializer(serializers.Serializer):
    maximum = serializers.IntegerField()
    minimum = serializers.IntegerField()
    average = serializers.IntegerField()
    median = serializers.IntegerField()
