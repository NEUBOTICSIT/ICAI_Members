# Generated by Django 4.1.3 on 2022-12-01 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Info_App', '0010_alter_personal_info_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personal_info',
            old_name='address',
            new_name='proof_address',
        ),
        migrations.RenameField(
            model_name='personal_info',
            old_name='area',
            new_name='proof_area',
        ),
        migrations.RenameField(
            model_name='personal_info',
            old_name='city',
            new_name='proof_city',
        ),
        migrations.RenameField(
            model_name='personal_info',
            old_name='pin_code',
            new_name='proof_pin_code',
        ),
        migrations.AddField(
            model_name='personal_info',
            name='blood_group',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='personal_info',
            name='residential_address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='personal_info',
            name='residential_area',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='personal_info',
            name='residential_city',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='personal_info',
            name='residential_pin_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]