from django.urls import path
from . import views


urlpatterns = [
    path('', views.ExpenseListAPIView.as_view(), name='expense' ),
    path("<int:id>", views.ExpenseDetailsAPIView.as_view(), name="expense-detail")
]
