# Generated by Django 4.2.4 on 2023-08-09 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rap', '0002_alter_member_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='paid',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
