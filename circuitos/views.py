# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ReservaForm
from django.template.context import RequestContext
#decorador para solicitar el login en cada accion
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def addreserva(request):
    if request.POST:
        form = ReservaForm(request.POST, request.FILES)
        if form.is_valid():
            reserva = form.save(commit = False)
            reserva.usuario = request.user
            reserva.save()
            return HttpResponseRedirect("/")
    else:
        form = ReservaForm()
    template = "circuitos/reservaform.html"
    return render(request,template,context_instance=RequestContext(request,locals()))

