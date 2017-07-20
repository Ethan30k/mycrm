#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout


def acc_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        print("res", user.userprofile.name)
        if user:
            #auth pass
            login(request, user)
            return redirect("/crm")

    return render(request, "login.html")


def acc_logout(request):
    logout(request)
    return redirect("/login")