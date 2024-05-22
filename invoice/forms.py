from datetime import datetime

from django.forms import fields, ModelForm
from django import forms

from formset.collection import FormCollection
from formset.renderers.bootstrap import FormRenderer
from formset.fieldset import Fieldset, FieldsetMixin
from formset.utils import FormMixin
from formset.widgets import Selectize
from .models import *

