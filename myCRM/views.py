#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import string

from django.contrib.auth import authenticate, login, logout
from django.core.cache import cache
from django.shortcuts import render, redirect

from freeadmin import verify_code
from myCRM import settings


def verify_code_gen():
    filename = "".join(random.sample(string.ascii_lowercase + string.digits, 6))

    code = verify_code.gene_code("%s/statics/verify_code/" % settings.BASE_DIR, filename)
    cache.set(filename, code, 30)
    return code, filename


def acc_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        verify_key = request.POST.get("verify_key")
        verify_code_val = request.POST.get("verify_code")
        matched_code = False
        if cache.get(verify_key) is None:
            return redirect("/login")
        if cache.get(verify_key).lower() == verify_code_val.lower():  # pass 验证码
            matched_code = True
        else:
            code, filename = verify_code_gen()
            return render(request, "login.html", {'code_filename': filename,
                                                  'error': '验证码错误'})

        user = authenticate(username=username, password=password)
        print("res", user.userprofile.name)
        if user:
            # auth pass
            login(request, user)
            return redirect("/freeadmin")

    code, filename = verify_code_gen()

    return render(request, "login.html", {'code_filename': filename})


def acc_logout(request):
    logout(request)
    return redirect("/login")