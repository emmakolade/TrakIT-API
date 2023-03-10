from django.shortcuts import render
from rest_framework.views import APIView
import datetime
from expenses.models import Expense
from income.models import Income
from rest_framework import status, response
# Create your views here.


class ExpenseSumaryStats(APIView):
    def get_amount_for_category(self, expense_list, category):
        expense = expense_list.filter(category=category)
        amount = 0

        for expense in expense:
            amount += expense.amount

        return {'amount': str(amount)}

    def get_category(self, expense):
        return expense.category

    def get(self, request):
        todays_date = datetime.date.today()
        one_year_ago = todays_date-datetime.timedelta(days=360)
        expenses = Expense.objets.filter(
            user=request.user, date_gte=one_year_ago, date_lte=todays_date)

        final = {}
        categories = list(set(map(self.get_category, expenses)))

        for expense in expenses:
            for category in categories:
                final[category] = self.get_amount_for_category(
                    expenses, category)
        return response.Response({'category_data': final}, status=status.HTTP_200_OK)


class IncomeSumaryStats(APIView):
    def get_amount_for_source(self, income_list, source):
        income = income_list.filter(source=source)
        amount = 0

        for i in income:
            amount += income.amount

        return {'amount': str(amount)}

    def get_source(self, income):
        return income.source

    def get(self, request):
        todays_date = datetime.date.today()
        one_year_ago = todays_date-datetime.timedelta(days=360)
        income = Income.objets.filter(
            user=request.user, date_gte=one_year_ago, date_lte=todays_date)

        final = {}
        sources = list(set(map(self.get_source, income)))

        for i in income:
            for source in sources:
                final[source] = self.get_amount_for_source(
                    income, source)
        return response.Response({'income_data': final}, status=status.HTTP_200_OK)
