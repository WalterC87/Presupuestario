# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ProveedoresForm, PlanDeCuentasForm
from django.template.context import RequestContext

#from django.template.context import RequestContext

# Create your views here.
class login(TemplateView):
	template_name = 'bases/login.html'


def addproveedor(request):
    if request.POST:
        form = ProveedoresForm(request.POST, request.FILES)
        if form.is_valid():
            # lo valido, lo agrego pero no lo mando a bbdd
            proveedor = form.save(commit = False)
            #proveedor.usuario = request.user
            proveedor.save()
            return HttpResponseRedirect("/")
    else:
        form = ProveedoresForm()
    template = "bases/proveedoresform.html"
    return render(request,template,context_instance=RequestContext(request,locals()))

def addcuenta(request):
	if request.POST:
		form = PlanDeCuentasForm(request.POST, request.FILES)
		if form.is_valid():
			cuenta = form.save(commit=False)
			cuenta.save()
			return HttpResponseRedirect("/")
	else:
		form = PlanDeCuentasForm()
	template = "bases/cuentasform.html"
	return render(request, template,context_instance=RequestContext(request,locals()))