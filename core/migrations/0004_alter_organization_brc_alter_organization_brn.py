# Generated by Django 5.0.3 on 2024-03-09 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_billing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='brc',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='brn',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
