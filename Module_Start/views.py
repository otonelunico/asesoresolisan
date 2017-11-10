from django.shortcuts import render, redirect
from .forms import PageForm, ContactForm
from django.views import View
from .models import Page
from django.core.mail import EmailMessage
from django.template.loader import get_template
from services.settings import EMAIL_TO
from django.contrib.auth import logout as auth_logout


from django.utils.safestring import mark_safe
# Create your views here.

class Index(View):
    template = 'module_start/index.html'

    def get(self, request):
        page = Page.objects.last()
        page.title = mark_safe(page.title)
        page.us = mark_safe(page.us)
        page.note = mark_safe(page.note)
        page.service_one = mark_safe(page.service_one)
        page.service_two = mark_safe(page.service_two)
        page.reference_one = mark_safe(page.reference_one)
        page.reference_two = mark_safe(page.reference_two)
        page.reference_tree = mark_safe(page.reference_tree)
        form = ContactForm()
        return render(request, self.template, locals())

    def post(self, request, **kwargs):
        page = Page.objects.last()
        page.title = mark_safe(page.title)
        page.us = mark_safe(page.us)
        page.note = mark_safe(page.note)
        page.service_one = mark_safe(page.service_one)
        page.service_two = mark_safe(page.service_two)
        page.reference_one = mark_safe(page.reference_one)
        page.reference_two = mark_safe(page.reference_two)
        page.reference_tree = mark_safe(page.reference_tree)
        form = ContactForm(request.POST)
        print(EMAIL_TO)
        if form.is_valid():
            obj = form.save(commit=False)
            template = get_template('module_start/email.html')
            context = {'name': obj.name,
                       'rut': obj.rut,
                       'email': obj.email,
                       'city': obj.city,
                       'phone': obj.phone,
                        'gender' : obj.gender,
                       'prevision': obj.prevision ,
                        'message': obj.message
                       }
            content = template.render(context)
            for email in EMAIL_TO:
                msg = EmailMessage(obj.name+' '+obj.rut+' Se esta contactando por intermedio de la pagina web',
                                   content,
                                    "contacto@rosystems.cl",
                                    to = [email])
            msg.content_subtype = 'html'
            msg.send()
            print('envia ->'+ str(context))
            #send_ = True
            form.save()
            return redirect('module_start:home')
        else:
            form = PageForm()
            print(form.is_valid())
            print(form.errors)
        return render(request, self.template, locals())

class Admin(View):
    template = 'module_start/index.html'

    def get(self, request):
        form = PageForm()
        #print(form)
        page = Page.objects.last()
        page.title = mark_safe(page.title)
        page.us = mark_safe(page.us)
        page.note = mark_safe(page.note)
        page.reference_one = mark_safe(page.reference_one)
        page.reference_two = mark_safe(page.reference_two)
        page.reference_tree = mark_safe(page.reference_tree)
        admin = True
        return render(request, self.template, locals())

    def post(self, request, **kwargs):
        page = Page.objects.last()
        page.title = mark_safe(page.title)
        page.us = mark_safe(page.us)
        page.note = mark_safe(page.note)
        page.reference_one = mark_safe(page.reference_one)
        page.reference_two = mark_safe(page.reference_two)
        page.reference_tree = mark_safe(page.reference_tree)
        form = PageForm(request.POST, request.FILES)
        admin = True
        if form.is_valid():
            obj = form.save(commit=False)
            print(obj.us_img1)
            print(obj.us_img2)
            if obj.us_img1 == 'us_img1.png':
                obj.us_img1 = page.us_img1
            if obj.us_img2 == 'us_img2.png':
                obj.us_img2 = page.us_img2
            form.save()
            auth_logout(request)
            return redirect('module_start:home')
        else:
            form = PageForm()
            print(form.is_valid())
            print(form.errors)
        return render(request, self.template, locals())