from django.db import models


class Tables(models.Model):
    name = models.TextField(
        help_text="Название",
        verbose_name="Название"
    )
    business_name = models.TextField(
        help_text="Бизнес название",
        verbose_name="Бизнес название",
        null=True,
        blank=True
    )
    color = models.TextField(
        help_text="Цвет",
        verbose_name="Цвет",
        default="#fff",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tables"
        verbose_name = "Таблица"
        verbose_name_plural = "Таблицы"