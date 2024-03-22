from django.shortcuts import render, redirect
from django.http import HttpResponse
# from autenticacao_app.models import User
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def user_cadastro(request):

    if request.method == 'GET':
        return render(request, 'cadastro.html')
    
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username):
            messages.error(request, 'Usuário já cadastrado!')
            return redirect('cadastro')
        
        if len(username)>10:
            messages.error(request, 'O seu nome de usuário deve ter no máximo 10 caracteres.')
            return redirect('cadastro')
        
        if username.isnumeric():
            messages.error(request, 'O nome de usuário não pode conter apenas números.')
            return redirect('cadastro')

        user = User.objects.create_user(username=username, password=password)
        user.save()

        messages.success(request, 'Cadastro concluído com sucesso.')
        return redirect('login')
        
def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    elif request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_django(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Credenciais incorretas')
            return redirect('/auth/login')
            
def user_signout(request):
    pass

@login_required(login_url='/auth/login')
def home(request):
    return render(request, 'home.html')
