from django.shortcuts import render
from django.http import HttpResponse

from . models import People, VisRate, Profession

# Create your views here.

def index(request):
    #return HttpResponse("Главная")
    return render(request, 'index.html')

def ourStaff(request):
    staff = People.objects.all()
    staff_cnt = staff.count()

    profs = Profession.objects.all()

    print(profs, staff)
    return render(request, 'staf.html', context={"staff": staff, "profs": profs})