# Generated by Django 4.0.4 on 2022-07-04 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontur_mailey', '0003_alter_filtername_options_remove_filtername_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filtername',
            options={'verbose_name': 'Фильтр', 'verbose_name_plural': 'Фильтры'},
        ),
        migrations.AddField(
            model_name='filtername',
            name='name',
            field=models.CharField(max_length=254, null=True, verbose_name='Название фильтра'),
        ),
    ]
