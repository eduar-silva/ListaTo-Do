from django.http import HttpResponse

def index_view(request:HttpResponse):
    return HttpResponse("<h1>Seja bem-vindo</h1><a href='tarefas'>Visualizar Tarefas</a>")