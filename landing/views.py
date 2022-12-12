from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.core import serializers
from django.http.response import JsonResponse
from django.core.serializers import serialize
import json

from landing.models import News
from landing.forms import NewsForm

# Create your views here.
def showLanding(request):
    dataNews = News.objects.all()
    context = {
        'listDataNews' : dataNews,
    }
    return render(request, "landing.html", context)

def addNews(request):
    form = NewsForm()
    if request.method == "POST":
        form = NewsForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            dataNews = News()
            dataNews.title = form.cleaned_data['title']
            dataNews.description = form.cleaned_data['description']
            dataNews.save()
            
            return HttpResponseRedirect(reverse('landing:showLanding'))

    return render(request, 'formPage.html', {'form': form})

def getAddNews(request):
    print("PASS")
    if request.method == 'GET':
            #data = json.loads(request.body)
            #user_id = data['user_id']
            #try:
                #user =  User.objects.get(username=user_id)
                #print(user_id)
                dataNews = News.objects.all()
                if dataNews is not None:
                    serialized_data = serialize("json", dataNews)
                    serialized_data = json.loads(serialized_data)
                    return JsonResponse(serialized_data, safe=False, status=200)
                else:
                    return JsonResponse({"instance": "Gagal, data tidak ditemukan"}, status=404)

            #xcept User.DoesNotExist:
            #    return JsonResponse({"instance": "Gagal, data tidak ditemukan"}, status=404)