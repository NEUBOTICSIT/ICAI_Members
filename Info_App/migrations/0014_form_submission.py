# Generated by Django 4.1.6 on 2023-02-04 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Info_App', '0013_rename_proof_pin_code_personal_info_holding_cop_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='form_submission',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('member_firstname', models.CharField(blank=True, max_length=100, null=True)),
                ('member_lastname', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('membership_number', models.CharField(blank=True, max_length=100, null=True)),
                ('year_of_membership', models.CharField(blank=True, max_length=100, null=True)),
                ('Phone_number', models.CharField(blank=True, max_length=100, null=True)),
                ('photo', models.ImageField(blank=True, default='', null=True, upload_to='Info_App/image/')),
                ('prof_address', models.CharField(blank=True, max_length=500, null=True)),
                ('prof_area', models.CharField(blank=True, max_length=500, null=True)),
                ('prof_city', models.CharField(blank=True, max_length=500, null=True)),
                ('prof_pin_code', models.CharField(blank=True, max_length=100, null=True)),
                ('residential_address', models.CharField(blank=True, max_length=500, null=True)),
                ('residential_area', models.CharField(blank=True, max_length=500, null=True)),
                ('residential_city', models.CharField(blank=True, max_length=500, null=True)),
                ('residential_pin_code', models.CharField(blank=True, max_length=100, null=True)),
                ('corr_prof_address', models.CharField(blank=True, default=' ', max_length=500, null=True)),
                ('corr_prof_area', models.CharField(blank=True, default=' ', max_length=500, null=True)),
                ('corr_prof_city', models.CharField(blank=True, default=' ', max_length=500, null=True)),
                ('corr_prof_pin_code', models.CharField(blank=True, default=' ', max_length=100, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=10, null=True)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('DOM', models.DateField(blank=True, null=True)),
                ('email_id', models.EmailField(blank=True, max_length=100, null=True)),
                ('organization', models.CharField(blank=True, max_length=500, null=True)),
                ('holding_COP', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=100)),
            ],
        ),
    ]
