#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django import forms
from crm import models


class EnrollmentForm(forms.ModelForm):
    def __new__(cls, *args, **kwargs):
        for field_name, field_obj in cls.base_fields.items():
            field_obj.widget.attrs['class'] = 'form-control'
        return forms.ModelForm.__new__(cls)

    class Meta:
        model = models.Enrollment
        exclude = ['enrollment_date', 'contract_agreed', 'contract_approved']


class CustomerForm(forms.ModelForm):
    def __new__(cls, *args, **kwargs):
        disabled_fields = ['consultant', 'referral_from', 'source']

        for field_name, field_obj in cls.base_fields.items():
            field_obj.widget.attrs['class'] = 'form-control'
            if field_name in disabled_fields:
                field_obj.widget.attrs['disabled'] = True
        return forms.ModelForm.__new__(cls)

    class Meta:
        model = models.Customer
        # fields = "__all__"
        exclude = ['consult_content', 'status', 'consult_courses']


class CustomerForm2(forms.ModelForm):
    def __new__(cls, *args, **kwargs):

        for field_name, field_obj in cls.base_fields.items():
            field_obj.widget.attrs['class'] = 'form-control'

        return forms.ModelForm.__new__(cls)

    class Meta:
        model = models.Customer
        fields = "__all__"
        # exclude = ['consult_content', 'status', 'consult_courses']


class EnrollmentForm2(forms.ModelForm):
    def __new__(cls, *args, **kwargs):
        for field_name, field_obj in cls.base_fields.items():
            field_obj.widget.attrs['class'] = 'form-control'
        return forms.ModelForm.__new__(cls)

    class Meta:
        model = models.Enrollment
        # fields = "__all__"
        exclude = ['customer']
