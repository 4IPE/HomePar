from django.shortcuts import render,redirect
from .forms import UserForm,SupportForm,CityForm,RoomForm,LowForm,HighForm
from .models import City,Room,Low,High
from pars.cian import maincian



#Обработчик главной страницы
def  index(request):
    error=''
    if request.method=="POST":
        formcity=CityForm(request.POST)
        formroom=RoomForm(request.POST)
        formlow=LowForm(request.POST)
        formhigh=HighForm(request.POST)
        if formcity.is_valid() and formroom.is_valid() and formlow.is_valid() and formhigh.is_valid():
            formcity.save()
            formroom.save()
            formlow.save()
            formhigh.save()
            return redirect('result')
        else:
            error='Ошибка заполнения '
    formcity=CityForm()
    formroom=RoomForm()
    formlow=LowForm()
    formhigh=HighForm()
    data={
        'formcity':formcity,
        'formroom':formroom,
        'formlow':formlow,
        'formhigh':formhigh,
        'error':error,
    }
    return render(request,'homeparapp/index.html',data)



#Обработчик  страницы о нас 
def about(request):
    return render(request,'homeparapp/about.html')



#Обработчик  страницы подписки
def price (request):
   return render(request,'homeparapp/price.html')


#Обработчик  страницы с выводом результата
def result (request):
       info_city=City.objects.order_by("city")[:1].get()
       info_s=Room.objects.all().order_by("room")[:1].get()
       info_price_low=Low.objects.all().order_by("price_low")[:1].get()
       info_price_high=High.objects.all().order_by("price_high")[:1].get()
       maincian(info_city,info_s,info_price_low,info_price_high)
       return render(request,'homeparapp/result.html')

#Обработчик  страницы помощи
def support (request):
    error=''
    if request.method=="POST":
        form=SupportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thx')
        else:
            error='Ошибка заполнения '
    form=SupportForm()
    sup={
        'form':form,
        'error':error
    }
    return render(request,'homeparapp/support.html',sup)


#Обработчик  страницы входа
def singin (request):
    error=''
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error='Ошибка заполнения '
    form=UserForm()

    us={
        'form':form,
        'error':error
    }
    return render(request,'homeparapp/singin.html',us)


#Обработчик  страницы благодарства о отправленом вопросом
def thx(request):
    return render(request,'homeparapp/thx.html')
