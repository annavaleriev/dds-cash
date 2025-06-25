from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from dds_app.models import CashFlow, Category, Status, Subcategory, Type


class StatusSerializer(serializers.ModelSerializer):
    """Сериализатор для статусов операций"""

    class Meta:
        model = Status
        fields = "__all__"


class TypeSerializer(serializers.ModelSerializer):
    """Сериализатор для типов операций"""

    class Meta:
        model = Type
        fields = "__all__"


class SubcategorySerializer(serializers.ModelSerializer):
    """Сериализатор для подкатегорий операций"""

    class Meta:
        model = Subcategory
        fields = "__all__"


class CategoryBaseSerializer(serializers.ModelSerializer):
    """Базовый сериализатор для категорий"""

    type = TypeSerializer(label="Тип операции")
    subcategory = SubcategorySerializer(many=True, label="Подкатегории операции")

    class Meta:
        model = Category
        fields = ("id", "name", "type", "subcategory")


class CategoryCreateSerializer(CategoryBaseSerializer):
    """Сериализатор для создания категорий"""

    subcategory = serializers.PrimaryKeyRelatedField(
        queryset=Subcategory.objects.all(), many=True, help_text="Выберите подкатегории операции"
    )

    type = serializers.PrimaryKeyRelatedField(queryset=Type.objects.all(), help_text="Выберите тип операции")

    def validate(self, attrs):
        """Проверка валидности данных"""
        validated_data = super().validate(attrs)
        if not validated_data.get("subcategory"):
            raise ValidationError({"subcategory": "Выберите хотя бы одну подкатегорию операции"})
        return validated_data

    def create(self, validated_data):
        """Создание категории с подкатегориями"""
        subcategories = validated_data.pop("subcategory")
        category = Category.objects.create(**validated_data)
        category.subcategory.set(subcategories)
        return category

    def update(self, instance, validated_data):
        """Обновление категории и подкатегорий"""

        subcategory = validated_data.pop("subcategory", None)
        if subcategory is not None:
            instance.subcategory.set(subcategory)
        return super().update(instance, validated_data)


class CashFlowCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CashFlow
        fields = "__all__"
        read_only_fields = ("created_at",)

    def validate(self, data):
        """Проверка, что категория соответствует типу операции"""

        type = data.get("type")
        category = data.get("category")

        if category and type and category.type != type:
            raise ValidationError({"category": "Категория должна соответствовать типу операции"})

        return data

    def validate_amount(self, value):
        """Проверка, что сумма операции больше нуля"""
        if value <= 0:
            raise ValidationError({"amount": "Сумма операции должна быть больше нуля"})
        return value


class CashFlowSerializer(CashFlowCreateSerializer):
    """Сериализатор для операций с денежными средствами"""

    status = StatusSerializer(label="Статус операции")
    type = TypeSerializer(label="Тип операции")
    category = CategoryBaseSerializer(label="Категория операции")
    subcategory = SubcategorySerializer(label="Подкатегория операции")
