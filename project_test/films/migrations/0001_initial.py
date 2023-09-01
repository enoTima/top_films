# Generated by Django 4.2 on 2023-04-29 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=128)),
                ('last', models.CharField(blank=True, max_length=128, null=True)),
                ('portrait', models.ImageField(blank=True, null=True, upload_to='portraits/')),
            ],
        ),
    ]