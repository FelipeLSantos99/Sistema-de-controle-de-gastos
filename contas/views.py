from django.shortcuts import render, redirect
from .models import Transacao
import datetime
from .form import TransacaoForm


def home(request):
    now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    return render(request, 'contas/home.html')

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)

def nova_transacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        transacao = form.save()
        return redirect('url_listagem')  # redireciona para listagem

    data['form'] = form
    return render(request, 'contas/form.html', data)

def update(request, pk):
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form
    data['transacao'] = transacao
    return render(request, 'contas/form.html', data)

def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_listagem')