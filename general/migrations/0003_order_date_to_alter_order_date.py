# Generated by Django 5.2b1 on 2025-03-07 13:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_rename_servicetypes_typesofservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_to',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(),
        ),
    ]
