# Generated by Django 5.0.3 on 2024-11-24 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_footearse'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_image', models.ImageField(upload_to='static/')),
            ],
        ),
        migrations.DeleteModel(
            name='Footearse',
        ),
    ]
