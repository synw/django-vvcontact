# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class vvContactConfig(AppConfig):
    name = "vvcontact"
    verbose_name = _(u"Contact form")
    
    def ready(self):
        pass