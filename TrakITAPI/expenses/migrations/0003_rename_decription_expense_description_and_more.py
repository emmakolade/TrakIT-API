# Generated by Django 4.1.5 on 2023-01-23 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_alter_expense_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='decription',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
