# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.http.response import Http404
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from vvcontact.models import Email
from vvcontact.forms import EmailForm
from vvcontact.conf import SAVE_TO_DB, RECIPIENTS_LIST


class OkPageView(TemplateView):
    template_name = "vvcontact/rest_ok.html"
    

class AddPostView(CreateView):
    model = Email
    form_class = EmailForm
    
    def form_valid(self, form, **kwargs):
        if self.request.method == "POST":
            obj = form.save(commit=False)
            obj.email = form.cleaned_data['email']
            obj.subject = form.cleaned_data['subject']
            obj.content = form.cleaned_data['content']
            formated_request = ''
            for key in self.request.META.keys():
                formated_request += str(key)+' : '+str(self.request.META[key])+'\n'
            obj.request = formated_request
            #~ send mail
            send_mail(obj.subject, obj.content, obj.email, RECIPIENTS_LIST)
        else: 
            raise Http404
        if SAVE_TO_DB == True:
            return super(AddPostView, self).form_valid(form)
        else:
            return
    
    def get_success_url(self):
        return "/contact/ok/"


class AddPostRestView(AddPostView):
    
    def get_template_names(self):
        return ['vvcontact/rest_form.html']
