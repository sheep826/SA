from django.shortcuts import render
from .models import price
from django.http import HttpResponse
from .form import order_detailModelForm
# Create your views here.
def index(request):
    return render(request, "index.html")

def dinosaur(request):
    return render(request, "dinosaur.html")

def wash1(request):
    return render(request, "wash1.html")

def wash2(request):
    if request.method == 'POST':
        mode_wash = request.POST.get('wash')
        #mode_spin = request.POST.get('spin')
        #mode_dry = request.POST.get('dry')
        #mode_fold = request.POST.get('fold')
        print(mode_wash)
        #print(mode_spin)
        #print(mode_dry)
        #print(mode_fold)
        form = order_detailModelForm()
        context = {'form': form}
        return render(request, "wash2.html")
    elif request.method == 'GET':
        return render(request, "wash2.html")

def order(request):
    return render(request, "order.html")

def QA(request):
    return render(request, "QA.html")

def contact(request):
    return render(request, "contact.html")

def order_detail(request):
    return render(request, "order_detail.html")

def QRcode(request):
    return render(request, 'QRcode.html')

def transmode1(request):
    return render(request, 'transmode1.html')

def transmode2(request):
    return render(request, 'transmode2.html')