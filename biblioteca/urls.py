from django.urls import path
from .views import upload_excel, LivroListView, LivroDetailView

urlpatterns = [
    path('upload/', upload_excel, name='upload'),
    path('', LivroListView.as_view(), name='livro_list'),
    path('<int:pk>/', LivroDetailView.as_view(), name='livro_detail'),
]