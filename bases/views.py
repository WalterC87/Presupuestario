# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response
from django.views.generic import TemplateView 

# Create your views here.
class login(TemplateView):
	template_name = 'bases/login.html'
