from rest_framework.routers import DefaultRouter


from dds_app.views import StatusViewSet, TypeViewSet, SubcategoryViewSet, CategoryViewSet, CashFlowViewSet

router = DefaultRouter()

router.register(r"status", StatusViewSet)
router.register(r"type", TypeViewSet)
router.register(r"subcategory", SubcategoryViewSet)
router.register(r"category", CategoryViewSet)
router.register(r"cash-flow", CashFlowViewSet)

urlpatterns = router.urls
