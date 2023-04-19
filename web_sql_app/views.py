from django.shortcuts import render
from django.views import View
from django.db import connection
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from .forms import Sp_get_amcom, Sp_get_talon, Sp_accept_amcom_pay, SignInForm
from .models import Sale


class MainView(View): 
    def get(self, request, *args, **kwargs):
        form = SignInForm()
        return render(request, 'web_sql_app/signin.html', context={
        'form': form,}
        )
    def post(self, request, *args, **kwargs):
        form = SignInForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('home')
        return render(request, 'web_sql_app/signin.html', context={
            'form': form,
        })

class HomeView(View): 
    def get(self, request, *args, **kwargs):
        return render(request, 'web_sql_app/home.html', context={
        })

class Sp_Get_AmcomView(View):
    def get(self, request, *args, **kwargs):
        form = Sp_get_amcom()
        if 'amcom' in request.session:
            ds_query = request.session['amcom']
            paginator = Paginator(ds_query, 2)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, 'web_sql_app/sp_get_amcom.html', context={
            'form': form, 'page_obj': page_obj,
            })
        else: 
            return render(request, 'web_sql_app/sp_get_amcom.html', context={
                'form': form, 
        })


    def post(self, request, *args, **kwargs):
        form = Sp_get_amcom(request.POST)
        params = (request.POST.get('fcard'), request.POST.get('ncard'), request.POST.get('scard'))
        if form.is_valid():
            try:
                cursor = connection.cursor()
                cursor.execute("{CALL dbo.sp_get_amcom_V2 (%s, %s, %s)}", params)
                columns = [col[0] for col in cursor.description]
                col = [dict(zip(columns, row)) for row in cursor.fetchall()]
                cursor.cancel() 
            except Exception:
                print("Ошибка базы данных")

            request.session['amcom'] = col
            paginator = Paginator(col, 2)
            page = request.GET.get('page')
            page_obj = paginator.get_page(page)
            
            return render(request, 'web_sql_app/sp_get_amcom.html', context={
                'form': form, 'page_obj': page_obj,
            })

   
class Sp_Get_TalonView(View):
    def get(self, request, *args, **kwargs):
        form = Sp_get_talon()
        if 'talon' in request.session:
            ds_query = request.session['talon']
            paginator = Paginator(ds_query, 2)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            return render(request, 'web_sql_app/sp_get_talon.html', context={
            'form': form, 'page_obj': page_obj,
            })
        else:    
            return render(request, 'web_sql_app/sp_get_talon.html', context={
                'form': form, 
        })

    def post(self, request, *args, **kwargs):
        form = Sp_get_talon(request.POST)
        #temp = request.POST
        #params = []
        #for tmp in temp:
        #    if tmp != 'csrfmiddlewaretoken':
        #        params.append(request.POST.get(tmp))
        params = (request.POST.get('fcard'), request.POST.get('ncard'), request.POST.get('scard'))
        if form.is_valid():
            try:
                cursor = connection.cursor()
                cursor.execute("{CALL dbo.sp_get_talon (%s, %s, %s)}", params)
                columns = [col[0] for col in cursor.description]
                col = [dict(zip(columns, row1)) for row1 in cursor.fetchall()]
                cursor.cancel() 
            except Exception:
                print("Ошибка базы данных")

            request.session['talon'] = col
            paginator = Paginator(col, 2)
            page = request.GET.get('page')
            page_obj = paginator.get_page(page)
            
            return render(request, 'web_sql_app/sp_get_talon.html', context={
                    'form': form, 'page_obj': page_obj,
            })

class Sp_Accept_Amcom_PayView(View):
    def get(self, request, *args, **kwargs):
        form = Sp_accept_amcom_pay()
        sale = Sale.objects.all().order_by('-date')
        
        paginator = Paginator(sale, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'web_sql_app/sp_accept_amcom_pay.html', context={
            'form': form, 'page_obj': page_obj,
        })

    def post(self, request, *args, **kwargs):
        form = Sp_accept_amcom_pay(request.POST)
        params = (request.POST.get('fcard'), request.POST.get('ncard'), request.POST.get('amcom'),
                  request.POST.get('kassid'), request.POST.get('sum'), request.POST.get('data'),
                  request.POST.get('vid'), request.POST.get('kol'))
        #if form.is_valid():
        try:
            cursor = connection.cursor()
            cursor.execute("{CALL dbo.sp_accept_amcom_pay (%s, %s, %s, %s, %s, %s, %s, %s)}", params)
            cursor.cancel() 
        except Exception:
            return render(request, 'web_sql_app/block/prompt.html', context={
            'prompt': 'Ошибка базы данных'})
        return render(request, 'web_sql_app/block/prompt.html', context={
            'prompt': 'Запись добавлена', 'form': form,})
    

