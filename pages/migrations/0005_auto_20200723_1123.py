# Generated by Django 3.0.8 on 2020-07-23 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_category_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='cid',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pages.category'),
        ),
    ]
