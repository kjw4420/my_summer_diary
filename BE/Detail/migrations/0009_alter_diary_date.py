# Generated by Django 4.2.1 on 2023-06-05 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Detail', '0008_alter_diary_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
