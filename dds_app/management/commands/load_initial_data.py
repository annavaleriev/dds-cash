from django.core.management import BaseCommand

from dds_app.models import Category, Status, Subcategory, Type


class Command(BaseCommand):
    help = "Загрузка начальных данных в базу"
    statuses = ("Поступление", "Списание")
    categories = [
        {"name": "Инфраст", "subcategories": [{"name": "VPS"}, {"name": "Proxy"}]},
        {"name": "123123213", "subcategories": [{"name": "123124124125412"}, {"name": "5123521512512"}]},
    ]

    def handle(self, *args, **kwargs):
        status_instances = [Status(name=status_name) for status_name in self.statuses]

        Status.objects.bulk_create(status_instances, ignore_conflicts=True)

        category_type, _ = Type.objects.get_or_create("Выполнено")

        for category in self.categories:
            instance, _ = Category.objects.get_or_create(name=category["name"], type=category_type)
            subcategories = []
            for subcategory in category["subcategories"]:
                subcategory_instance, _ = Subcategory.objects.get_or_create(name=subcategory["name"])
                subcategories.append(subcategory_instance)
            instance.set(subcategories)

        Type.objects.get_or_create(name="Поступление")
        Type.objects.get_or_create(name="Списание")

        for status in ["Бизнес", "Личное", "Налог"]:
            Status.objects.get_or_create(name=status)

        infrastructure_category, _ = Category.objects.get_or_create(name="Инфраструктура")
        marketing_category, _ = Category.objects.get_or_create(name="Маркетинг")

        for name in ["VPS", "Proxy"]:
            Subcategory.objects.get_or_create(name=name, category=infrastructure_category)
        for name in ["Farpost", "Avito"]:
            Subcategory.objects.get_or_create(name=name, category=marketing_category)

        self.stdout.write(self.style.SUCCESS("Начальные данные успешно загружены."))
