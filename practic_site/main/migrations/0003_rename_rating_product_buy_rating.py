# Generated by Django 4.0.4 on 2022-05-31 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_categoty_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='rating',
            new_name='buy_rating',
        ),
    ]
