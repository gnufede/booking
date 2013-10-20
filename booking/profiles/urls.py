# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.core.urlresolvers import reverse_lazy

from profiles.views import *

urlpatterns = patterns(
    '',
    url(r'^profile/$', profile,
        name='profile'),
    url(r'^user_home/$', user_home,
        name='user_home'),
)
