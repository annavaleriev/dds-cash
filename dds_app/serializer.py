from rest_framework import serializers

from dds_app.models import Status


class StatusSerializer(serializers.ModelSerializer):
    """Сериализатор для статусов операций"""

    class Meta:
        model = Status
        fields = "__all__"


class TypeSerializer(serializers.ModelSerializer):
    """Сериализатор для типов операций"""

    class Meta:
        model = Status
        fields = "__all__"
