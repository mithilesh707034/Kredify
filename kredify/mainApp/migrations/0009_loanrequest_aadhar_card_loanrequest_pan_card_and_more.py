# Generated by Django 4.1.1 on 2022-12-17 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0008_rename_application_loanrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanrequest',
            name='aadhar_card',
            field=models.FileField(blank=True, default='', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='pan_card',
            field=models.FileField(blank=True, default='', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='photo',
            field=models.ImageField(blank=True, default='', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='salary_sleep',
            field=models.FileField(blank=True, default='', null=True, upload_to=''),
        ),
    ]