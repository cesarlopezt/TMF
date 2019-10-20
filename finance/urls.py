from django.urls import path
from . import views
from .views import MovementListView, MovementCreateView

urlpatterns = [
    path('', MovementListView.as_view(), name='finance-home'),
    # path('Movement/<int:pk>/', MovementDetailView.as_view(), name='movement-detail'),
    path('Movement/new/', MovementCreateView.as_view(), name='movement-create'),
]