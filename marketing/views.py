from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import View, TemplateView
from .forms import MessageForm
from django.template.response import TemplateResponse
from django.urls import reverse, reverse_lazy


class HomePageView(View):
    def get(self, request):
       return  TemplateResponse(request, "marketing/home.html", {})

    def post(self, request):
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse_lazy('success'))


class SuccessPageView(TemplateView):
    template_name = 'marketing/success.html'



