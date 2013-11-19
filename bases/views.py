from django.shortcuts import render_to_response
from django.views.generic import TemplateView 

# Create your views here.
class login(TemplateView):
	template_name = 'bases/login.html'

class index2(TemplateView):
	template_name = 'bases/index2.html'