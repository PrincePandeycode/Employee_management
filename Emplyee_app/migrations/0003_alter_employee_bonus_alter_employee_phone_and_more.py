# Generated by Django 4.1.7 on 2023-12-13 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Emplyee_app', '0002_alter_employee_bonus_alter_employee_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(default=0),
        ),
    ]
