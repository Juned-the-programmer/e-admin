# Generated by Django 3.0.8 on 2020-07-21 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='static/images/LRM_EXPORT_183111279742168_20190116_174312437.jpeg', upload_to=''),
        ),
    ]