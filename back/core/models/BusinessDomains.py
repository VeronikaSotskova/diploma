from django.db import models


class BusinessDomains(models.Model):
    name = models.TextField(
        help_text="Название",
        verbose_name="Название"
    )
    description = models.TextField(
        help_text="Описание",
        verbose_name="Описание",
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
    tables = models.ManyToManyField(
        to="core.Tables",
        related_name="business_domains",
        related_query_name="business_domains",
        through="core.TablesInDomains"
    )
    parent = models.ForeignKey(
        to="self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
        related_query_name="children",
        db_column="parent_id"
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "business_domains"
        verbose_name = "Бизнес домен"
        verbose_name_plural = "Бизнес домены"
