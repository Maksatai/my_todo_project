# Generated by Django 3.1.5 on 2021-01-22 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210122_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='books',
            name='description',
            field=models.TextField(),
        ),
    ]