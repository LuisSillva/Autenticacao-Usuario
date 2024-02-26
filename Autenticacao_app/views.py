from django.shortcuts import render, redirect
from django.http import HttpResponse
# from Autenticacao_app.models import User
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required


def user_cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse('Esse usuário já existe.')
        
        user = User.objects.create_user(username=username, password=password)
        user.save()

        return HttpResponse('Usuário cadastrado com sucesso.')
        
def user_login(request):

    if request.method == 'GET':
        return render(request, 'login.html')

    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login_django(request, user)

            return HttpResponse('Autenticado')
        else:
            return HttpResponse('Usuário não encontrado')

@login_required(login_url='/auth/login')
def home(request):
    return HttpResponse('Home ^^')
