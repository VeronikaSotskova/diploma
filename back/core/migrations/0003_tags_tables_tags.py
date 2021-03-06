# Generated by Django 4.0.3 on 2022-04-17 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_tablesindomains_business_domain_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(help_text='Название', verbose_name='Название')),
                ('description', models.TextField(help_text='Описание', verbose_name='Описание')),
                ('color', models.TextField(blank=True, default='#fff', help_text='Цвет', null=True, verbose_name='Цвет')),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
                'db_table': 'tags',
            },
        ),
        migrations.AddField(
            model_name='tables',
            name='tags',
            field=models.ManyToManyField(related_name='tables', related_query_name='tables', to='core.tags'),
        ),
    ]
