from email.errors import MessageError
from turtle import title
from django.shortcuts import redirect, render
from.models import Artiles
from django.contrib import messages
from .forms import UserRegisterForm




# Create your views here.




def register(request):
    if request.method== 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"ВЫ ЗАРЕГЕСТРИРОВАНЫ!")
            return redirect ('login')
        else:
            messages.error(request,"ОШИБКА РЕГИСТРАЦИИ!!(введите данные корректно)")
    else:
        form=UserRegisterForm()
    form=UserRegisterForm()
    return render(request,'tatooshi/register.html',{'form':form})

def login(request):
    return render(request,'tatooshi/login.html')




def lilo(request):
 
    return render(request, 'tatooshi/HT.html')




def index(request):
    data={
        'title':'SOCIALNYE SETI',
    }

    return render(request,'tatooshi/soc.seti.html',data)







def test(request):
    otzyv=Artiles.objects.order_by("-date")
    return render(request,'tatooshi/otzyv.html',{'otzyv':otzyv})







def test1(request):
    return render(request,'tatooshi/zayavka.html')