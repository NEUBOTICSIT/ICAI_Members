# Generated by Django 4.1.6 on 2023-03-03 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Info_App', '0018_remove_form_submission_corr_prof_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form_submission',
            name='membership_number',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
    ]
