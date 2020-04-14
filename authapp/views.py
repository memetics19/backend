from django.shortcuts import render
import hashlib

def Authentication(request):
    password=get.Password()

    result=hashlib.md5(password.encode())
