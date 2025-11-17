<<<<<<< HEAD
<<<<<<< HEAD
from django.urls import path, include
from . import views

app_name = 'tarefas'

"""direcionamento do usuário aos caminhos escritos"""
urlpatterns = [
    #página inicial
    path('', views.index, name="index"),
    #página com visualização das tarefas pendentes
    path('home/', views.home_app, name="home"),

    #redirecionamento da página da adição de uma tarefa e atualização das tarefas
    path('adicionar/', views.TarefaCreateView.as_view(), name="adicionar"),
    path('remover/<int:id>', views.tarefa_remover, name="remover"),
    path('editar/<int:id>', views.tarefa_editar, name="editar"),

    #faz a checkbox referente a "situação" da tabela
    path('toggle/<int:id>/', views.toggle_tarefa, name="toggle"),

    #faz o redirecionamento para página de atividades completas a partir do momento que a checkbox é marcada
    path('completas/', views.tarefas_concluidas, name="completas")
=======
=======
>>>>>>> f6c29825cea240311fcef022460126e90bbca9fb
from django.urls import path
from . import views

app_name = "tarefas"

urlpatterns = [
    path("", views.tarefas_home, name="home"),
    path("adicionar/", views.tarefas_adicionar, name="adicionar"),
    path("remover/<int:id>", views.tarefa_remover, name="remover"),
    path("editar/<int:id>", views.tarefa_editar, name="editar")
<<<<<<< HEAD
>>>>>>> f6c29825cea240311fcef022460126e90bbca9fb
=======
>>>>>>> f6c29825cea240311fcef022460126e90bbca9fb
]