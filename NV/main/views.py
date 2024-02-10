from django.shortcuts import render
from django.http import HttpResponse

from . models import People, VisRate, Profession

# Create your views here.

def index(request):
    return render(request, 'index.html')

def ourStaff(request):
    staff = People.objects.all()
    staff_cnt = staff.count()

    profs = Profession.objects.all()

    print(profs, staff)
    return render(request, 'staf.html', context={"staff": staff, "profs": profs})

def ourVac(request):
    profs = Profession.objects.all()

    prof_names = list()
    for prof in profs:
        prow_worker_cnt = str(len(People.objects.filter(profile=prof)))
        prof_names.append([prof.profession, prow_worker_cnt])

    return render(request, 'profs.html', context={"profs": prof_names, "title": "Работники"})

