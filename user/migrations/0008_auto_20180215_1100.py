# Generated by Django 2.0.2 on 2018-02-15 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_student_stu_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='stu_image_url',
            field=models.CharField(default='/static/images/nit.png', max_length=300),
        ),
    ]
