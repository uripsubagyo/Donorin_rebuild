from django.shortcuts import render
from django.shortcuts import render, redirect
from jadwal.models import Jadwal
from jadwal.forms import JadwalForm
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json
from django.core.exceptions import ObjectDoesNotExist
from django.core.serializers import serialize

# Create your views here.

@login_required(login_url='/signin/')
def show_jadwal(request):
    jadwal = Jadwal.objects.filter(user=request.user)
    context = {
        'list_jadwal': jadwal
    }

    return render(request, 'jadwal.html', context)

def get_jadwal(request):
    data_jadwal = serializers.serialize("json", Jadwal.objects.filter(user=request.user))
    return HttpResponse(data_jadwal, content_type="application/json")

@login_required(login_url='/signin/')
def delete(request, id):
    Jadwal.objects.get(id=id).delete()
    return redirect('jadwal:show_jadwal')

@login_required(login_url='/signin/')
def book_jadwal(request):
    if request.method == 'POST':
        form = JadwalForm(request.POST)
        if form.is_valid():
            tanggal = form.cleaned_data['tanggal']
            lokasi = form.cleaned_data['lokasi']

            Jadwal.objects.create(user=request.user, date=tanggal, loc=lokasi)

            return HttpResponseRedirect(reverse('jadwal:show_jadwal'))
    else:
        form = JadwalForm()
    context = {'form':form}
    return render(request, 'book.html', context)
    # return JsonResponse({'instance': 'Jadwal Dibuat'}, status=200)

def show_location(request):
    return render(request, 'location.html')
# Create your views here.

def show_jadwal_json(request):
    data = Jadwal.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def add_jadwal_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        tanggal = data['tanggal_donor']
        lokasi = data['lokasi_donor']
        user_id = data['user_id']
        user =  User.objects.get(id = user_id)
        if user is not None:
            if user.is_active:
                new_id = User.objects.get(id = user_id).pk
                try:
                    jadwals = Jadwal.objects.all()
                    if jadwals is not None:
                        last_jadwal_id = Jadwal.objects.latest('id').pk
                        for j in jadwals:
                            if (j.tanggal_donor == tanggal) and (j.user == user):
                                return JsonResponse({"instance": "Pilih tanggal lain"}, status=400)
                        
                        jadwal_baru = Jadwal(last_jadwal_id+1, new_id, tanggal, lokasi)
                except ObjectDoesNotExist:
                    last_jadwal_id = 1
                    jadwal_baru = Jadwal(last_jadwal_id+1, new_id, tanggal, lokasi)
                
                jadwal_baru.save()
                return JsonResponse({"instance": "Jadwal berhasil dibuat"}, status=200)

        else:
            return JsonResponse({
                "status": False,
                "message": "Login Failed"
            }, status=401)

@csrf_exempt
def delete_jadwal_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        jadwal_id = data['jadwal_id']
        try:
            jadwal = Jadwal.objects.get(id=jadwal_id)
            if jadwal is not None:
                jadwal.delete()
                return JsonResponse({"instance": "Berhasil menghapus jadwal"}, status=200)
            else:
                return JsonResponse({"instance": "Gagal, data tidak ditemukan"}, status=404)

        except ObjectDoesNotExist:
            return JsonResponse({"instance": "Gagal, data tidak ditemukan"}, status=404)

@csrf_exempt
def get_jadwal_user(request):
    if request.method == 'POST':
            data = json.loads(request.body)
            user_id = data['user_id']
            try:
                user =  User.objects.get(username=user_id)
                print(user_id)
                jadwal = Jadwal.objects.filter(user=user)
                if jadwal is not None:
                    serialized_data = serialize("json", jadwal)
                    serialized_data = json.loads(serialized_data)
                    return JsonResponse(serialized_data, safe=False, status=200)
                else:
                    return JsonResponse({"instance": "Gagal, data tidak ditemukan"}, status=404)

            except User.DoesNotExist:
                return JsonResponse({"instance": "Gagal, data tidak ditemukan"}, status=404)