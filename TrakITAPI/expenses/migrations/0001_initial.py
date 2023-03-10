# Generated by Django 4.1.5 on 2023-01-20 21:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('ONLINE_SERVICES', 'ONLINE_SERVICES'), ('FOOD', 'FOOD'), ('HOUSING', 'HOUSING'), ('TRANSPORTATION', 'TRANSPORTATION'), ('UTILITIES', 'UTILITIES'), ('INSURNACE', 'INSURNACE'), ('MEDICAL', 'MEDICAL'), ('SAVINGS AND INVESTMENT', 'SAVINGS AND INVESTMENT'), ('PERSONAL_CARE', 'PERSONAL_CARE'), ('LIFESTYLE', 'LIFESTYLE'), ('TRAVEL', 'TRAVEL'), ('EMERGENCYFUND', 'EMERGENCYFUND'), ('DEBT_PAYMENT', 'DEBT_PAYMENT')], max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, max_length=255)),
                ('decription', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
