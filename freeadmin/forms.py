#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from crm import models
from django.utils.translation import ugettext as _


def CreateModelForm(request, admin_obj):
    class Meta:
        model = admin_obj.model
        fields = "__all__"

    def __new__(cls, *args, **kwargs):
        print(cls.base_fields.items())
        for field_name, field_obj in cls.base_fields.items():
            field_obj.widget.attrs['class'] = 'form-control'
            if field_name in admin_obj.readonly_fields:
                field_obj.widget.attrs['disabled'] = True
        return forms.ModelForm.__new__(cls)

    def default_clean(self):
        # print("default clean:", self)
        for field in admin_obj.readonly_fields:
            print("readonly:", field, self.instance)
            field_val_from_db = getattr(self.instance, field)
            field_val = self.cleaned_data.get(field)
            if field_val_from_db == field_val:
                print("field not change")
            else:
                self.add_error(field, '"%s" readonly field, value should be %s' % (field, field_val_from_db))
        print("cleaned data:", self.cleaned_data)

    dynamic_model_form = type("DynamicModelForm", (forms.ModelForm,), {"Meta": Meta})
    setattr(dynamic_model_form, "__new__", __new__)
    setattr(dynamic_model_form, "clean", default_clean)
    return dynamic_model_form

