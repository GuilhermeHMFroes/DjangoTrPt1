from django.shortcuts import render, get_object_or_404
from trabalho.models import Aluno
from .forms import ContatoForm
from django.contrib import messages

# Create your views here.

def index(request):

    alunos = Aluno.objects.all()

    testChave = {
        'alunos': alunos
    }

    return render(request, 'index.html', testChave)

def aluno(request, nome):

    aluno = get_object_or_404(Aluno, nome=nome)
    context = {
        'aluno': aluno
    }

    return render(request, 'aluno.html', context)

def contato(request):

    form = ContatoForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.send_mail()
            form = ContatoForm()
            messages.success(request, 'E-mail enviado com sucesso!')

    context={
        'form':form
    }

    return render(request, 'contato.html', context)

