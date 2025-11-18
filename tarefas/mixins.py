from django.contrib.auth.mixins import LoginRequiredMixin

"""criação de mensagem personalizada ao tentar acessar sem estar logado"""
class TarefaLoginRequiredMixin(LoginRequiredMixin):
    permission_denied_message = "Você precisa estar logado para visualizar ou criar tarefas"