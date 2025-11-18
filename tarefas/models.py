from django.db import models
from django.contrib.auth.models import User

"""
Definição do modelo de Tarefa no banco de dados.
Inclui o campo 'owner' para atribuir a tarefa a um usuário específico.
"""


class TarefaModel(models.Model):
    # Campos de Tarefa
    tarefa = models.CharField(max_length=100)  # Nome/Título da tarefa
    descricao = models.TextField(null=True, blank=True)  # Descrição opcional (da segunda versão)
    feito = models.BooleanField(default=False)  # Status de conclusão (feito/concluido)

    # Datas
    data_criacao = models.DateTimeField(auto_now_add=True)  # Data de criação
    prazo_final = models.DateTimeField(null=True, blank=True)  # Prazo final
    data_conclusao = models.DateTimeField(null=True, blank=True)  # Data de conclusão

    # Relação com Usuário
    """criação do usuário para atribuir as tarefas a um só usuário"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    """retornar o título da tarefa para apresentação visual"""

    def __str__(self):
        return self.title