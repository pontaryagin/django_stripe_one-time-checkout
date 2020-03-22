from rest_framework import serializers

class StripeConfigSerializer(serializers.Serializer):
    """Your data serializer, define your fields here."""
    publicKey = serializers.CharField(max_length=100)
    basePrice = serializers.IntegerField()
    currency = serializers.CharField()
