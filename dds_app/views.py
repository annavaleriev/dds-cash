from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from dds_app.models import CashFlow, Category, Status, Subcategory, Type
from dds_app.permissions import IsOwnerOnly
from dds_app.serializer import (
    CashFlowCreateSerializer,
    CashFlowSerializer,
    CategoryBaseSerializer,
    CategoryCreateSerializer,
    StatusSerializer,
    SubcategorySerializer,
)


class StatusViewSet(ModelViewSet):
    """ViewSet для статусов"""

    queryset = Status.objects.all().order_by("name")
    serializer_class = StatusSerializer
    permission_classes = [IsAuthenticated]


class TypeViewSet(ModelViewSet):
    """ViewSet для типов"""

    queryset = Type.objects.all().order_by("name")
    serializer_class = StatusSerializer
    permission_classes = [IsAuthenticated]


class SubcategoryViewSet(ModelViewSet):
    """ViewSet для подкатегорий"""

    queryset = Subcategory.objects.all().order_by("name")
    serializer_class = SubcategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category"]
    permission_classes = [IsAuthenticated]


class CategoryViewSet(ModelViewSet):
    """ViewSet для категорий"""

    queryset = Category.objects.all().order_by("name")
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["subcategory"]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        """Возвращает сериализатор в зависимости от действия"""
        if self.action in ["list", "retrieve"]:
            return CategoryBaseSerializer
        return CategoryCreateSerializer


class CashFlowViewSet(ModelViewSet):
    """ViewSet для денежных потоков"""

    queryset = CashFlow.objects.all().order_by("created_at")
    serializer_class = CashFlowSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["status", "type", "category", "subcategory"]
    permission_classes = [IsAuthenticated, IsOwnerOnly]

    def get_serializer_class(self):
        serializer_class = super().get_serializer_class()
        if self.request.method in SAFE_METHODS:
            return serializer_class
        return CashFlowCreateSerializer

    def get_queryset(self):
        """Возвращает данные только если он владелец"""
        return self.queryset.filter(user=self.request.user)
