from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse


def index(request):
    template = 'index.html'
    if request.method == 'GET':
        return render(request, template)
    elif request.method == 'POST':
        name = request.POST.get('name-of-form')
        return render(request, template, context={'name': name})


def ajax(request):
    import time
    time.sleep(3)
    name = request.GET.get('name')
    return HttpResponse(f'こんにちは、{name}さん！')
