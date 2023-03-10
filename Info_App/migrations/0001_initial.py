# Generated by Django 4.1.3 on 2022-11-28 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal_Info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('member_name', models.CharField(max_length=100)),
                ('membership_number', models.CharField(max_length=20)),
                ('Phone_number', models.CharField(max_length=11)),
                ('email_id', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('photo', models.ImageField(default='', upload_to='Personal_Info/images/')),
                ('DOB', models.DateField()),
                ('DOM', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
