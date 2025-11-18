from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TarefaForm
from .models import TarefaModel
from django.http import HttpRequest
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django import forms
# Presume que este mixin existe para proteger CreateView
from .mixins import TarefaLoginRequiredMixin
from django.utils import timezone

"""
Backend da criação, remoção e atualização das tarefas, e também, da checkbox.
Após a conclusão, todas as funções redirecionam o usuário para a página de visualização de tarefas completas ou pendentes.
"""


# Página inicial (landing page)
def index(request):
    """Página de boas-vindas."""
    return render(request, 'tarefas/index.html')


# Página inicial de visualização das tarefas pendentes
# O @login_required força o usuário a estar logado para acessar
@login_required
def home_app(request: HttpRequest):
    """
    Exibe a lista de tarefas pendentes do usuário logado, 
    ordenadas pelo prazo final.
    """
    # Filtra tarefas que pertencem ao usuário logado e que não foram feitas (feito=False)
    # Note que o nome do campo 'feito' é da versão original do seu código.
    tarefas_pendentes = TarefaModel.objects.filter(owner=request.user, feito=False).order_by('prazo_final')
    contexto = {
        'tarefas': tarefas_pendentes,
    }
    return render(request, 'tarefas/home_tarefas.html', contexto)


# Criação de Tarefas usando Class-Based View (CBV)
class TarefaCreateView(TarefaLoginRequiredMixin, CreateView):
    """View para criar uma nova tarefa e atribuí-la ao usuário logado."""
    model = TarefaModel
    form_class = TarefaForm
    success_url = reverse_lazy('tarefas:home')
    template_name = 'tarefas/adicionar.html'

    # Sobrescreve para atribuir a tarefa ao usuário logado antes de salvar
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


# Backend da remoção de tarefas
@login_required
def tarefa_remover(request: HttpRequest, id):
    """Remove uma tarefa específica do banco de dados."""
    # Busca a tarefa pelo ID, garantindo que ela pertença ao usuário logado (segurança)
    tarefa = get_object_or_404(TarefaModel, id=id, owner=request.user)
    tarefa.delete()
    return redirect("tarefas:home")


# Backend da edição de tarefas
@login_required
def tarefa_editar(request: HttpRequest, id):
    """Permite a edição de uma tarefa existente."""
    # Busca a tarefa pelo ID, garantindo que ela pertença ao usuário logado (segurança)
    tarefa = get_object_or_404(TarefaModel, id=id, owner=request.user)

    if request.method == "POST":
        formulario = TarefaForm(request.POST, instance=tarefa)
        if formulario.is_valid():
            formulario.save()
            # Redireciona para home ou para completas, dependendo do status atual
            if tarefa.feito:
                return redirect("tarefas:completas")
            return redirect("tarefas:home")
    else:
        formulario = TarefaForm(instance=tarefa)

    context = {
        "form": formulario,
        "tarefa": tarefa
    }
    return render(request, 'tarefas/editar.html', context)


# Backend da checkbox (toggle)
@login_required
def toggle_tarefa(request, id):
    """Alterna o status de conclusão de uma tarefa."""
    tarefa = get_object_or_404(TarefaModel, id=id, owner=request.user)

    if request.method == 'POST':
        # Verifica se o campo 'completo' foi enviado no POST (se a checkbox foi marcada)
        completo = 'completo' in request.POST

        tarefa.feito = completo

        if tarefa.feito:
            # Se foi concluída, define a data de conclusão para agora
            tarefa.data_conclusao = timezone.now()
            tarefa.save()
            return redirect('tarefas:completas')
        else:
            # Se foi desmarcada, remove a data de conclusão
            tarefa.data_conclusao = None
            tarefa.save()
            return redirect('tarefas:home')

    # Caso a requisição não seja POST, apenas redireciona para a home
    return redirect("tarefas:home")


# Acesso à página de tarefas concluídas
@login_required
def tarefas_concluidas(request: HttpRequest):
    """Exibe a lista de tarefas concluídas do usuário logado."""
    # Filtra tarefas que pertencem ao usuário logado e que foram feitas (feito=True)
    # Note que o nome do campo 'feito' é da versão original do seu código.
    tarefas_completas = TarefaModel.objects.filter(owner=request.user, feito=True).order_by('prazo_final')

    context = {
        'tarefas': tarefas_completas
    }
    return render(request, 'tarefas/completas.html', context)