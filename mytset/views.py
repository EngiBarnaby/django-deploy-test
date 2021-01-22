from django.shortcuts import render
from django.http import JsonResponse


def testFunc(request):
    test = {"title": "JSON response from django app"}
    return JsonResponse(test)

