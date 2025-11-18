from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

"""Backend do logout e register"""
#aqui é onde o logout ocorre através de uma função já existente do django, após a conclusão o usuário é enviado a página principal
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('tarefas:index'))

#onde ocorre o registro do usuário, onde ao final ele é logado e mandado a tela inicial
def register(request):
    if request.method != 'POST':
        form = UserCreationForm()

    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            novo_user = form.save()

            authenticated_user = authenticate(username=novo_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('tarefas:index'))

    context = {
        'form' : form
    }
    return render(request, 'users/register.html', context)