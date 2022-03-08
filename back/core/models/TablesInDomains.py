from django.db import models


class TablesInDomains(models.Model):
    table = models.ForeignKey(
        to="core.Tables",
        on_delete=models.CASCADE,
        db_column="table_id",
        related_query_name="tables_in_domains",
        related_name="tables_in_domains",
    )
    business_domain = models.ForeignKey(
        to="core.BusinessDomains",
        on_delete=models.CASCADE,
        db_column="domain_id",
        related_query_name="tables_in_domains",
        related_name="tables_in_domains",
    )

    class Meta:
        db_table = "tables_in_domains"
        verbose_name = "Таблица связка таблиц и доменов"
        verbose_name_plural = "Таблица связка таблиц и доменов"
