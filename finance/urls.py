from django.urls import path
from .views import MovementListView, ExpenseCreateView, IncomeCreateView
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('', MovementListView.as_view(), name='finance-home'),
    path('add/Expense/', ExpenseCreateView.as_view(), name='expense-create'),
    path('add/Income/', IncomeCreateView.as_view(), name='income-create')
]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)