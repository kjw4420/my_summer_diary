# Generated by Django 4.2.1 on 2023-06-05 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Detail', '0007_alter_diary_drawing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='date',
            field=models.DateField(blank=True, default=' ', null=True),
        ),
    ]
