# Generated by Django 4.0.4 on 2022-07-04 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontur_mailey', '0004_alter_filtername_options_filtername_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emails',
            options={'verbose_name': 'Емэйл', 'verbose_name_plural': 'Емэйлы'},
        ),
        migrations.AddField(
            model_name='filtername',
            name='need_to_send',
            field=models.BooleanField(default=False),
        ),
    ]
