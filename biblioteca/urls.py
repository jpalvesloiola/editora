from django.urls import path
from .views import LivroListView, LivroDetailView

urlpatterns = [
    path('', LivroListView.as_view(), name='livro_list'),
    path('<int:pk>/', LivroDetailView.as_view(), name='livro_detail'),
]