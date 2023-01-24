from .views import ExpenseSumaryStats, IncomeSumaryStats
from django.urls import path

urlpatterns = [
    path('expense_category_data', ExpenseSumaryStats.as_view(), name='expense_category_data'),
    path('income_sources_data', IncomeSumaryStats.as_view(),
         name='income_sources_data'),
]
