from django.shortcuts import render, redirect
from .forms import PageForm, ContactForm
from django.views import View
from .models import Page
from django.core.mail import EmailMessage
from django.template.loader import get_template
from services.settings import EMAIL_TO
from django.contrib.auth import logout as auth_logout

import cloudinary
import cloudinary.uploader
import cloudinary.api

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

        img = str(page.us_img1).split('.')
        page.us_img1 = mark_safe(cloudinary.CloudinaryImage(img[0] + '.' + img[1]).image(width=200, height=200, crop="fill"))
        img = str(page.us_img2).split('.')
        page.us_img2 = mark_safe(cloudinary.CloudinaryImage(img[0] + '.' + img[1]).image(width=200, height=200, crop="fill"))
        img = str(page.service_img).split('.')
        page.service_img = mark_safe(cloudinary.CloudinaryImage(img[0] + '.' + img[1]).image())

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

        img = str(page.us_img1).split('.')
        page.us_img1 = mark_safe(cloudinary.CloudinaryImage(img[0] + '.' + img[1]).image(width=200, height=200, crop="fill"))
        img = str(page.us_img2).split('.')
        page.us_img2 = mark_safe(cloudinary.CloudinaryImage(img[0] + '.' + img[1]).image(width=200, height=200, crop="fill"))
        img = str(page.service_img).split('.')
        page.service_img = mark_safe(cloudinary.CloudinaryImage(img[0] + '.' + img[1]).image())

        form = ContactForm(request.POST)
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
            emails = EMAIL_TO
            emails = emails.split(',')
            for email in emails:
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

        img = str(page.us_img1).split('.')
        page.us_img1 = mark_safe(cloudinary.CloudinaryImage(img[0] + '.' + img[1]).image(width=200, height=200, crop="fill"))
        img = str(page.us_img2).split('.')
        page.us_img2 = mark_safe(cloudinary.CloudinaryImage(img[0] + '.' + img[1]).image(width=200, height=200, crop="fill"))
        img = str(page.service_img).split('.')
        page.service_img = mark_safe(cloudinary.CloudinaryImage(img[0] + '.' + img[1]).image())

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

        img = str(page.us_img1).split('.')
        page.us_img1 = mark_safe(cloudinary.CloudinaryImage(img[0] + '.' + img[1]).image(width=200, height=200, crop="fill"))
        img = str(page.us_img2).split('.')
        page.us_img2 = mark_safe(cloudinary.CloudinaryImage(img[0] + '.' + img[1]).image(width=200, height=200, crop="fill"))
        img = str(page.service_img).split('.')
        page.service_img = mark_safe(cloudinary.CloudinaryImage(img[0] + '.' + img[1]).image())

        form = PageForm(request.POST, request.FILES)
        admin = True
        page = Page.objects.last()
        if form.is_valid():
            obj = form.save(commit=False)
            img1=True
            img2=True
            img3=True
            if obj.us_img1 == "":
                obj.us_img1 = page.us_img1
                img1=False
            if obj.us_img2 == "":
                obj.us_img2 = page.us_img2
                img2 = False
            if obj.service_img == "":
                obj.service_img = page.service_img
                img3 = False
            form.save()
            if img1:
                img = str(obj.us_img1).split('.')
                cloudinary.uploader.upload('media/' + str(obj.us_img1),
                                           public_id=str(img[0]))
            if img2:
                img = str(obj.us_img2).split('.')
                cloudinary.uploader.upload('media/'+str(obj.us_img2),
                                           public_id=str(img[0]))
            if img3:
                img = str(obj.service_img).split('.')
                cloudinary.uploader.upload('media/'+str(obj.service_img),
                                           public_id=str(img[0]))

            auth_logout(request)
            return redirect('module_start:home')
        else:
            form = PageForm()
            print(form.is_valid())
            print(form.errors)
        return render(request, self.template, locals())