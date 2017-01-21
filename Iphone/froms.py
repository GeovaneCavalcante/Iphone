from django import forms
class Meu_Form(forms.Form):
    seu_nome = forms.CharField(label='Seu nome', max_length=100)
    senha = forms.CharField(label='senha', max_length=100)