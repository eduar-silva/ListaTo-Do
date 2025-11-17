from django import forms
from .models import TarefaModel

<<<<<<< HEAD
<<<<<<< HEAD
"""criação das áreas a serem preenchidas nos formulários"""
class TarefaForm(forms.ModelForm):
    class Meta:
        model = TarefaModel
        fields = ['tarefa', 'prazo_final']

        """criação do widget para usar o calendário no momento de preencher o prazo final"""
        widgets = {
            'prazo_final': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'}),
        }
=======
class TarefaForm(forms.ModelForm):
    class Meta:
        model = TarefaModel
        fields = ['nome', 'descricao', 'concluido']
>>>>>>> f6c29825cea240311fcef022460126e90bbca9fb
=======
class TarefaForm(forms.ModelForm):
    class Meta:
        model = TarefaModel
        fields = ['nome', 'descricao', 'concluido']
>>>>>>> f6c29825cea240311fcef022460126e90bbca9fb
