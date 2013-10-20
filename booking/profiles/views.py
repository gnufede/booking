# coding: utf-8

from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response

@login_required
def profile(request):
    redirect_to = request.REQUEST.get('next', '/')
    return HttpResponseRedirect(redirect_to)

@login_required
def user_home(request):
    return render_to_response('profiles/user_home.html',
            None,
            context_instance=RequestContext(request))
