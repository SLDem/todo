# Generated by Django 5.0.1 on 2024-02-05 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_item_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.TextField(default='Pets', max_length=12),
            preserve_default=False,
        ),
    ]
