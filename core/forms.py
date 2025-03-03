from django import forms
from .models import Cliente, Obra

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cnpj', 'email', 'telefone', 'endereco']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'cnpj': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '00.000.000/0000-00'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(00) 00000-0000'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'exemplo@dominio.com'
            }),
            'endereco': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Logradouro, nº, Bairro, Cidade/UF'
            }),
        }

class ObraForm(forms.ModelForm):
    class Meta:
        model = Obra
        fields = '__all__'
        widgets = {
            'endereco_obra': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'cidade': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'tempo_obra': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'data_inicio': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'data_conclusao': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'valor_obra': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01'
            }),
            'status_parcelado': forms.RadioSelect(choices=[(True, 'Sim'), (False, 'Não')]),
            'status_parcelado': forms.RadioSelect(attrs={
                'class': 'form-check'
            }),
            'descricao': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }