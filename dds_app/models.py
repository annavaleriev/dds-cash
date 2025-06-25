from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Status(models.Model):
    """Модель для статусов операций"""

    name = models.CharField(max_length=100, verbose_name="Статус операции", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус операции"
        verbose_name_plural = "Статусы операций"
        ordering = ["name"]


class Type(models.Model):
    """Модель для типов операций"""

    name = models.CharField(max_length=100, verbose_name="Тип операции", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип операции"
        verbose_name_plural = "Типы операций"
        ordering = ["name"]


class Subcategory(models.Model):
    """Модель для подкатегорий операций"""

    name = models.CharField(max_length=100, verbose_name="Подкатегория операции")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Подкатегория операции"
        verbose_name_plural = "Подкатегории операций"
        ordering = ["name"]


class Category(models.Model):
    """Модель для категорий операций"""

    name = models.CharField(max_length=100, verbose_name="Категория операции")
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name="Тип операции")
    subcategory = models.ManyToManyField(
        Subcategory,
        verbose_name="Подкатегории операции",
        blank=True,
        help_text="Выберите подкатегории операции",
    )

    def __str__(self):
        return f"{self.name} {self.subcategory} {self.type}"

    class Meta:
        verbose_name = "Категория операции"
        verbose_name_plural = "Категории операций"
        ordering = ["name"]


class CashFlow(models.Model):
    """Модель для операций с денежными средствами"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="cash_flows")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name="Статус операции")
    type = models.ForeignKey(Type, on_delete=models.PROTECT, verbose_name="Тип операции")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория операции")
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name="Подкатегория операции")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма операции")
    comment = models.TextField(verbose_name="Комментарий", null=True, blank=True)

    def __str__(self):
        return f"{self.created_at} - {self.amount} - {self.type} - {self.category} - {self.subcategory}"

    class Meta:
        verbose_name = "Операция с денежными средствами"
        verbose_name_plural = "Операции с денежными средствами"
        ordering = ["-created_at"]
