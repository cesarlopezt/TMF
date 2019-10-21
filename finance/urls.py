from django.urls import path
from .views import MovementListView, ExpenseCreateView, IncomeCreateView

urlpatterns = [
    path('', MovementListView.as_view(), name='finance-home'),
    path('add/Expense/', ExpenseCreateView.as_view(), name='expense-create'),
    path('add/Income/', IncomeCreateView.as_view(), name='income-create')
]