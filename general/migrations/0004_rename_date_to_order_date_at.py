# Generated by Django 5.2b1 on 2025-03-07 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_order_date_to_alter_order_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='date_to',
            new_name='date_at',
        ),
    ]
