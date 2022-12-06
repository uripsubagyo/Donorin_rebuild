from django import forms
from datetime import datetime

def date_validator(tanggal):
	current = int(datetime.now().strftime("%j"))
	inp = int(tanggal.strftime("%j"))
	if inp <= current: raise forms.ValidationError("Masukkan tanggal yang akan datang")

loc = [
    ('PMI Provinsi DKI Jakarta', 'PMI Provinsi DKI Jakarta'),
    ('PMI Kota Jakarta Utara', 'PMI Kota Jakarta Utara'),
    ('PMI Kota Jakarta Pusat', 'PMI Kota Jakarta Pusat'),
    ('PMI Kota Jakarta Timur', 'PMI Kota Jakarta Timur'),
    ('PMI Kota Jakarta Barat', 'PMI Kota Jakarta Barat'),
    ('PMI Kota Jakarta Selatan', 'PMI Kota Jakarta Selatan'),
]

class JadwalForm(forms.Form):
    tanggal = forms.DateField(validators=[date_validator], widget=forms.DateTimeInput(attrs={'type':'date','class':'form-control'}))
    lokasi = forms.ChoiceField(choices=loc, widget=forms.Select(attrs={'class': 'form-control'}))