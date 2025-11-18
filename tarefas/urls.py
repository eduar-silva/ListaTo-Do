from django.urls import path
from . import views

# Define o namespace do aplicativo
app_name = 'tarefas'

"""Direcionamento do usuário aos caminhos escritos"""
urlpatterns = [
    # Página inicial (usada para landing page ou tela de boas-vindas)
    path('', views.index, name="index"),

    # Página principal do aplicativo, mostrando tarefas pendentes
    path('home/', views.home_app, name="home"),

    # Redirecionamento para a página de adição de uma tarefa
    # Usa a View baseada em Classe (CBV)
    path('adicionar/', views.TarefaCreateView.as_view(), name="adicionar"),

    # Ações CRUD em tarefas individuais
    path('remover/<int:id>/', views.tarefa_remover, name="remover"),
    path('editar/<int:id>/', views.tarefa_editar, name="editar"),

    # Ação para alternar o status (feito/não feito) de uma tarefa
    path('toggle/<int:id>/', views.toggle_tarefa, name="toggle"),

    # Redirecionamento para a página de atividades completas/concluídas
    path('completas/', views.tarefas_concluidas, name="completas")
]