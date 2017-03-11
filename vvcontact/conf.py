# -*- coding: utf-8 -*-

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy


SAVE_TO_DB = getattr(settings, 'VV_CONTACT_SAVE_TO_DB', True)

RECIPIENTS_LIST = getattr(settings, 'VV_CONTACT_RECIPIENTS_LIST', [settings.DEFAULT_FROM_EMAIL])

EMAIL_SENT_MESSAGE = getattr(settings, 'VV_CONTACT_EMAIL_SENT_MESSAGE', _(u'Your message has been sent'))
