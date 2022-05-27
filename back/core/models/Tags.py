from django.db import models


class Tags(models.Model):
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
    tag_type = models.ForeignKey(
        "core.TagsType",
        help_text="Тип тэга",
        verbose_name="Тип тэга",
        null=True,
        blank=True,
        related_name="tags",
        related_query_name="tags",
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tags"
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"
