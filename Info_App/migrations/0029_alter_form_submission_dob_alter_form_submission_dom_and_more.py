# Generated by Django 4.1.6 on 2023-03-10 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Info_App', '0028_form_submission_new_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form_submission',
            name='DOB',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='form_submission',
            name='DOM',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='form_submission',
            name='Phone_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='form_submission',
            name='blood_group',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='form_submission',
            name='email_id',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='form_submission',
            name='holding_COP',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='form_submission',
            name='member_firstname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='form_submission',
            name='member_lastname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='form_submission',
            name='member_middlename',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='form_submission',
            name='membership_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='form_submission',
            name='new_photo',
            field=models.ImageField(blank=True, null=True, upload_to='Info_App/images/'),
        ),
        migrations.AlterField(
            model_name='form_submission',
            name='organization',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='form_submission',
            name='photo',
            field=models.ImageField(blank=True, default='', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='form_submission',
            name='prof_address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='form_submission',
            name='prof_area',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='form_submission',
            name='prof_city',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='form_submission',
            name='prof_pin_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='form_submission',
            name='residential_address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='form_submission',
            name='residential_area',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='form_submission',
            name='residential_city',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='form_submission',
            name='residential_pin_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='form_submission',
            name='year_of_membership',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
