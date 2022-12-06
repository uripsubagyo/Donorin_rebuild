from django.shortcuts import render
from django.shortcuts import render, redirect
from jadwal.models import Jadwal
from jadwal.forms import JadwalForm
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

@login_required(login_url='/signin/')
def show_jadwal(request):
    jadwal = Jadwal.objects.filter(user=request.user)
    context = {
        'list_jadwal': jadwal
    }

    return render(request, 'jadwal.html', context)

@login_required(login_url='/signin/')
def delete(request, id):
    if Jadwal.objects.get(id=id).accepted == 'Menunggu konfirmasi':
        Jadwal.objects.get(id=id).delete()
    elif Jadwal.objects.get(id=id).accepted == 'Dikonfirmasi - menunggu kedatangan':
         return redirect('jadwal:show_jadwal')
    return redirect('jadwal:show_jadwal')

@login_required(login_url='/signin/')
def book_jadwal(request):
    if request.method == 'POST':
        form = JadwalForm(request.POST)
        if form.is_valid():
            tanggal = form.cleaned_data['tanggal']
            lokasi = form.cleaned_data['lokasi']

            Jadwal.objects.create(user=request.user, date=tanggal, loc=lokasi, accepted='Menunggu konfirmasi')

            return HttpResponseRedirect(reverse('jadwal:show_jadwal'))
    else:
        form = JadwalForm()
    context = {'form':form}
    return render(request, 'book.html', context)

def show_location(request):
    return render(request, 'location.html')