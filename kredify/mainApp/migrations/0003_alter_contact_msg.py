# Generated by Django 4.1.1 on 2022-11-11 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_rename_quiries_contact_msg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='msg',
            field=models.TextField(),
        ),
    ]
