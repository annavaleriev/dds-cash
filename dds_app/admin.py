from django.contrib import admin

from dds_app.models import CashFlow, Category, Status, Subcategory, Type


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "get_subcategory")
    search_fields = ("name", "type", "subcategory")
    list_filter = ("name", "type", "subcategory")

    def get_subcategory(self, obj):
        return ", ".join(sub.name for sub in obj.subcategory.all())


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)


@admin.register(CashFlow)
class CashFlowAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at", "status", "type", "category", "subcategory", "amount", "comment")
    search_fields = (
        "user__username",
        "status__name",
        "type__name",
        "category__name",
        "subcategory__name",
        "amount",
    )
    list_filter = ("user", "created_at", "status", "type", "category", "subcategory")
    date_hierarchy = "created_at"
