from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from dds_app.models import Status, Type
from dds_app.serializer import StatusSerializer


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


# class SubcategoryViewSet(ModelViewSet):
#     """ViewSet для подкатегорий"""
#     queryset =
#     serializer_class =
#     filter_backends =
#     filter_fields = ("categories_set")
#     permission_classes =
#
#
# class CategoryViewSet(ModelViewSet):
#     """ViewSet для категорий"""
#     queryset =
#     serializer_class =
#     filter_backends =
#     filter_fields = ("subcategory_set")
#     permission_classes =
#
#
# class CashFlowViewSet(ModelViewSet):
#     """ViewSet для денежных потоков"""
#     queryset =
#     serializer_class =
#     filter_backends =
#     filterset_class =
#     permission_classes =
