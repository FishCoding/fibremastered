from django.http import HttpResponse
from django.template import loader
# this import is copied from django/views/generic/edit.py
from django.forms import models as model_forms

from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.db.models import ManyToManyField, TextField
from django.views.generic import View, DetailView, UpdateView, DeleteView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.detail import SingleObjectMixin
from django.template import loader
from django.template.exceptions import TemplateDoesNotExist
from django.shortcuts import redirect
from django.http import Http404, HttpResponseRedirect
from django.apps import apps
from fibremastered.models import Site

import re
import os
import bleach


def index(request):
    template = loader.get_template('fibremastered/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def estudis_fib(request):
    template = loader.get_template('fibremastered/estudis/fib.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def research(request):
    template = loader.get_template('fibremastered/recerca.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def lafib(request):
    template = loader.get_template('fibremastered/fib.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def look_into_db(request, url):
    all=Site.objects.all()
    # Look into db for the webpages
    for site in all:
        pass
    return index(request)

