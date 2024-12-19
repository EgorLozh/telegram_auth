from rest_framework  import serializers


class TelegramUserSerializer(serializers.Serializer):
    telegram_id = serializers.IntegerField()
    username = serializers.CharField()
    first_name = serializers.CharField()
    token = serializers.CharField()
