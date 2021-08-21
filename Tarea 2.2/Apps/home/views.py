from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name='index.html'


class CreditosView(TemplateView):
    template_name='creditos.html'

    
class AdminView(TemplateView):
    template_name='admin.html'


class EstudiantesView(TemplateView):
    template_name='estudiantes.html'