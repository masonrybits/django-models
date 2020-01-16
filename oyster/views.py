from django.views.generic import TemplateView, ListView, DetailView
from .models import Post

class HomeView(TemplateView):
  template_name = 'home.html'
  model = Post

class MenuListView(ListView):
  template_name = 'list.html'
  model = Post

class MenuDetailView(DetailView):
  template_name = 'detail.html'
  model = Post