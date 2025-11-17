<<<<<<< HEAD
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required
=======
>>>>>>> f6c29825cea240311fcef022460126e90bbca9fb
=======
>>>>>>> f6c29825cea240311fcef022460126e90bbca9fb
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TarefaForm
from .models import TarefaModel
from django.http import HttpRequest
<<<<<<< HEAD
<<<<<<< HEAD
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .mixins import TarefaLoginRequiredMixin
from django.utils import timezone

"""
Backend da criação, remoção e atualização das tarefas, e também, da checkbox
Após a conclusão, todas as funções redirecionam o usuário para a página de visualização de tarefas completas ou pendentes
"""

#página inicial onde está escrito "Bem vindo"
def index(request):
    return render(request, 'tarefas/index.html')

#página inicial de visualização das tarefas, com elas sendo ordenadas baseado no prazo final
#o @login_required força o usuário estar logado para poder fazer uso do site
@login_required
def home_app(request):
    tarefas_pendentes = TarefaModel.objects.filter(owner=request.user, feito=False).order_by('prazo_final')
    contexto = {
        'tarefas': tarefas_pendentes,
    }
    return render(request, 'tarefas/home_tarefas.html', contexto)

#tarefas são criadas e mandadas ao banco de dados,e após a criação o usuário é mandado a página de visualização de suas tarefas
class TarefaCreateView(TarefaLoginRequiredMixin, CreateView):
    model = TarefaModel
    form_class = TarefaForm
    success_url = reverse_lazy('tarefas:home')
    template_name = 'tarefas/adicionar.html'
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

#backend da remoção de tarefas
=======
=======
>>>>>>> f6c29825cea240311fcef022460126e90bbca9fb

# Create your views here.

def tarefas_home(request):
    contexto = {
        "Nome": "x",
        "tarefas": TarefaModel.objects.all()
    }
    return render(request, 'tarefas/home.html', contexto)

def tarefas_adicionar(request:HttpRequest):
    if request.method == "POST":
        formulario = TarefaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("tarefas:home")

    contexto = {
        "form": TarefaForm
    }
    return render(request, "tarefas/adicionar.html", contexto)

<<<<<<< HEAD
>>>>>>> f6c29825cea240311fcef022460126e90bbca9fb
=======
>>>>>>> f6c29825cea240311fcef022460126e90bbca9fb
def tarefa_remover(request:HttpRequest, id):
    tarefa = get_object_or_404(TarefaModel, id=id)
    tarefa.delete()
    return redirect("tarefas:home")

<<<<<<< HEAD
<<<<<<< HEAD
#backend da edição de tarefas
#a função recebe o que está no banco de dados, apresenta na tela e depois é enviada novamente sobrescrevendo as informações antigas
=======
>>>>>>> f6c29825cea240311fcef022460126e90bbca9fb
=======
>>>>>>> f6c29825cea240311fcef022460126e90bbca9fb
def tarefa_editar(request:HttpRequest, id):
    tarefa = get_object_or_404(TarefaModel, id=id)
    if request.method == "POST":
        formulario = TarefaForm(request.POST, instance=tarefa)
        if formulario.is_valid():
            formulario.save()
            return redirect("tarefas:home")
<<<<<<< HEAD
<<<<<<< HEAD
    else:
        formulario = TarefaForm(instance=tarefa)

        context = {
            "form": formulario,
            "tarefa": tarefa
        }
        return render(request, 'tarefas/editar.html', context)

#backend da checkbox
#quando a checkbox é marcada recebe o valor de 'completo', se for completo, a caixa fica marcada e o usuário é redirecionado para as tarefas completas
#quando a checkbox é marcada, o formulário recebe a hora atual para ser usada nas badges de "concluída" e "entregue com atraso"
def toggle_tarefa(request, id):
    tarefa = get_object_or_404(TarefaModel, id=id)
    if request.method == 'POST':
        completo = 'completo' in request.POST
        tarefa.feito = completo
        if tarefa.feito:
            tarefa.data_conclusao = timezone.now()
        else:
            tarefa.data_conclusao = None
        tarefa.save()
        if tarefa.feito:
            return redirect('tarefas:completas')
        else:
            return redirect('tarefas:home')
    return redirect("tarefas:home")

#acesso a página de tarefas concluídas, onde as tarefas são organizadas baseadas no prazo final
@login_required
def tarefas_concluidas(request):
    tarefas_completas = TarefaModel.objects.filter(owner=request.user, feito=True).order_by('prazo_final')

    context = {
        'tarefas': tarefas_completas
    }
    return render(request, 'tarefas/completas.html', context)
=======
=======
>>>>>>> f6c29825cea240311fcef022460126e90bbca9fb
        
    formulario = TarefaForm(instance=tarefa)
    context = {
        "form": formulario
    }
<<<<<<< HEAD
    return render(request, 'tarefas/editar.html', context)
>>>>>>> f6c29825cea240311fcef022460126e90bbca9fb
=======
    return render(request, 'tarefas/editar.html', context)
>>>>>>> f6c29825cea240311fcef022460126e90bbca9fb
