from django.urls import path
from .views import HomeView, MenuListView, MenuDetailView

urlpatterns = [
  path('', HomeView.as_view(), name = 'home'),
  path('list/', MenuListView.as_view(), name = 'list'),
  path('detail/<int:pk>/', MenuDetailView.as_view(), name = 'detail'),
]