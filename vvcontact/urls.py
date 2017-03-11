# -*- coding: utf-8 -*-

from django.conf.urls import url
from vvcontact.views import AddPostRestView, OkPageView


urlpatterns = [
    url(r'^rest/$', AddPostRestView.as_view(), name="contact-rest"),
    url(r'^sent/$', OkPageView.as_view(), name="contact-ok"),
    ]