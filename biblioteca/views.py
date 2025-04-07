from django.shortcuts import render
from django.http import HttpResponse
from .models import Livro
from django.views.generic import ListView, DetailView
from django.db.models import Q
from biblioteca.utils.utils import importar_excel 

def home(request):
    return render(request, "home.html")


def upload_excel(request):
    if request.method == 'POST':
        arquivo_excel = request.FILES['arquivo_excel']
        importar_excel(arquivo_excel)
        return render(request, 'import_success.html')
    return render(request, 'upload_excel.html')


class LivroListView(ListView):
    model = Livro
    template_name = 'livros/livro_list.html'
    context_object_name = 'livros'
    paginate_by = 10  # opcional, para paginação

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q', None)
        if query:
            queryset = queryset.filter(
                Q(titulo__icontains=query) | Q(autores__icontains=query)
            )
        return queryset

class LivroDetailView(DetailView):
    model = Livro
    template_name = 'livros/livro_detail.html'

