# -*- coding: utf-8 -*-

import json
from django.http import JsonResponse
from django.middleware.csrf import CsrfViewMiddleware
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.http.response import Http404
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.utils.html import escape
from django.template import loader, Context
from vvcontact.models import Email
from vvcontact.forms import EmailForm
from vvcontact.conf import SAVE_TO_DB, RECIPIENTS_LIST


def check_csrf(request):
    reason = CsrfViewMiddleware().process_view(request, None, (), {})
    if reason:
        return False
    return True


class AddPostView(CreateView):
    model = Email
    form_class = EmailForm
    
    def post(self, request, *args, **kwargs):
        data = json.loads(self.request.body.decode('utf-8'))
        email = escape(data['email'])
        subject = escape(data['subject'])
        content = escape(data['content'])
        if check_csrf(request) == False:
            return JsonResponse({"error":1, "content":""})
        formated_request = ''
        for key in self.request.META.keys():
            formated_request += str(key)+' : '+str(self.request.META[key])+'\n'
        #~ send mail
        send_mail(subject, content, email, RECIPIENTS_LIST)
        if SAVE_TO_DB == True:
            Email.objects.create(email=email, content=content, subject=subject, request=formated_request)
        t = loader.get_template('vvcontact/rest_ok.html')
        c = Context({})
        rendered = t.render(c)
        return JsonResponse({"error":0, "content": rendered})


class AddPostRestView(AddPostView):
    
    def get_template_names(self):
        return ['vvcontact/rest_form.html']
