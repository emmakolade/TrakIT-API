from django.db import models
from authentication.models import User
# Create your models here.


class Expense(models.Model):
    CATEGORY_OPTIONS = [
        ('ONLINE_SERVICES', 'ONLINE_SERVICES'),
        ('FOOD', 'FOOD'),
        ('HOUSING', 'HOUSING'),
        ('TRANSPORTATION', 'TRANSPORTATION'),
        ('UTILITIES', 'UTILITIES'),
        ('INSURNACE', 'INSURNACE'),
        ('MEDICAL', 'MEDICAL'),
        ('SAVINGS AND INVESTMENT', 'SAVINGS AND INVESTMENT'),
        ('PERSONAL_CARE', 'PERSONAL_CARE'),
        ('LIFESTYLE', 'LIFESTYLE'),
        ('TRAVEL', 'TRAVEL'),
        ('EMERGENCYFUND', 'EMERGENCYFUND'),
        ('DEBT_PAYMENT', 'DEBT_PAYMENT'),

    ]

    category = models.CharField(choices=CATEGORY_OPTIONS, max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(null=False, blank=False)
