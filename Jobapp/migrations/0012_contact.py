# Generated by Django 4.0.3 on 2022-04-17 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobapp', '0011_alter_applylist_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=150)),
                ('Subject', models.CharField(max_length=150)),
                ('Message', models.CharField(max_length=150)),
            ],
        ),
    ]