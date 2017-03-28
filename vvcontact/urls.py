# -*- coding: utf-8 -*-

from django.conf.urls import url
from vvcontact.views import AddPostRestView


urlpatterns = [
    url(r'^rest/$', AddPostRestView.as_view(), name="contact-rest"),
    ]