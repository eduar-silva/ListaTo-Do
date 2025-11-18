from django import forms
from .models import TarefaModel

"""Criação das áreas a serem preenchidas nos formulários de criação e edição de tarefas."""
class TarefaForm(forms.ModelForm):
    class Meta:
        model = TarefaModel
        # Incluímos title, description e due_date (prazo_final)
        fields = ['tarefa', 'prazo_final']

        """Criação do widget para usar o calendário no momento de preencher o prazo final."""
        widgets = {
            'prazo_final':forms.DateTimeInput(attrs={
                'class':'form-control',
                'type':'datetime-local'}),
        }