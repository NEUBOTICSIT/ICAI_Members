# Generated by Django 4.1.6 on 2023-02-27 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Info_App', '0016_alter_form_submission_prof_pin_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='form_submission',
            name='member_middlename',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='personal_info',
            name='member_middlename',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
