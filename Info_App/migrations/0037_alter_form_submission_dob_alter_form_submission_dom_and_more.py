# Generated by Django 4.1.6 on 2023-03-10 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Info_App', '0036_form_submission_new_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form_submission',
            name='DOB',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='form_submission',
            name='DOM',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='form_submission',
            name='holding_COP',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='', max_length=50),
            preserve_default=False,
        ),
    ]