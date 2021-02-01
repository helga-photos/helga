from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse


import re
import os


def mainpage(request):

    context = {"navbar": None}
    return render(request, "mainpage/index.html", context)
