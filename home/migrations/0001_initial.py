# Generated by Django 3.1.2 on 2020-10-16 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=122)),
                ('Last_Name', models.CharField(max_length=122)),
                ('Contact_Tel', models.CharField(max_length=122)),
                ('Email', models.CharField(max_length=122)),
                ('Your_Feedback', models.TextField()),
            ],
        ),
    ]
