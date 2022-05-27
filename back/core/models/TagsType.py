from django.db import models


class TagsType(models.Model):
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

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tags_type"
        verbose_name = "Тип тэга"
        verbose_name_plural = "Типы тэгов"
