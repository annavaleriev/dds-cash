from django.contrib import admin

from dds_app.models import Status, Type, Category, Subcategory, CashFlow


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name", )

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name", )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "type")
    search_fields = ("name","type")
    list_filter = ("name","type")


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name",)
    list_filter = ("name",)


@admin.register(CashFlow)
class CashFlowAdmin(admin.ModelAdmin):
    list_display = ("created_at", "status", "type", "category", "subcategory", "amount", "comment")
    search_fields = ("created_at", "status__name", "type__name", "category__name", "subcategory__name", "amount")
    list_filter = ("created_at", "status", "type", "category", "subcategory")
    date_hierarchy = 'created_at'
