from django.shortcuts import render
from django.http import HttpResponseRedirect
from .froms import Meu_Form
from .models import Enviados
def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Meu_Form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            q = Enviados()
            q.email = form.data.get('seu_nome')
            q.senha = form.data.get('senha')
            q.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/index/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Meu_Form()

    return render(request, 'Iphone/index.html', {'form': form})