# Generated by Django 5.0.3 on 2024-11-21 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_alter_header_header_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicesection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_title', models.CharField(max_length=100)),
                ('service_icon', models.ImageField(upload_to='static/')),
                ('service_sub_title', models.CharField(max_length=100)),
                ('service_details', models.CharField(max_length=100)),
                ('service_learn_more', models.CharField(max_length=100)),
            ],
        ),
    ]