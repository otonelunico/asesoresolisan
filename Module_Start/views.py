from django.shortcuts import render, redirect
from .forms import PageForm
from django.views import View
from .models import Page

from django.utils.safestring import mark_safe
# Create your views here.

class Index(View):
    template = 'module_start/index.html'

    def get(self, request):
        page = Page.objects.last()
        page.note = mark_safe(page)
        return render(request, self.template, locals())

class Admin(View):
    template = 'module_start/index.html'

    def get(self, request):
        form = PageForm()
        page = Page.objects.last()
        page.note = mark_safe(page)
        admin = True
        return render(request, self.template, locals())

    def post(self, request, **kwargs):
        page = Page.objects.last()
        page.note = mark_safe(page)
        form = PageForm(request.POST)
        admin = True
        if form.is_valid():
            form.save()
            return redirect('module_start:home')
        else:
            print(form.is_valid())
            print(form.errors)
        return render(request, self.template, locals())