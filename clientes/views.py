from django.shortcuts import render, redirect, get_object_or_404
from .models import Pessoa
from .forms import PessoaForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.
@login_required
def lista_pessoas(request):
  pessoas = Pessoa.objects.all()
  return render(request, 'pessoas.html', {'pessoas': pessoas})

@login_required
def nova_pessoa(request):
  form = PessoaForm(request.POST or None, request.FILES or None)

  if form.is_valid():
    form.save()
    return redirect('lista_pessoas')

  return render(request, 'form_pessoa.html', {'form': form})

@login_required
def atualizar_pessoa(request, id):

  if not request.user.has_perm('clientes.change_pessoa'):
    return HttpResponse('403 Forbidden')
  elif not request.user.is_superuser:
    return HttpResponse('Não é superusuário.')

  pessoa = get_object_or_404(Pessoa, pk=id)
  form = PessoaForm(request.POST or None, request.FILES or None, instance=pessoa)

  if form.is_valid():
    form.save()
    return redirect('lista_pessoas')

  return render(request, 'form_pessoa.html', {'form': form})

@login_required
def deletar_pessoa(request, id):
  pessoa = get_object_or_404(Pessoa, pk=id)
  #form = PessoaForm(request.POST or None, request.FILES or None, instance=pessoa)

  if request.method == 'POST':
    pessoa.delete()
    return redirect('lista_pessoas')

  return render(request, 'confirmacao_delete_pessoa.html', {'pessoa': pessoa})

class ListaPessoas(ListView):
  model = Pessoa

class PessoaDetail(PermissionRequiredMixin, DetailView):
  model = Pessoa  
  permission_required = 'clientes.visualizar_pessoa_detail'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['now'] = timezone.now()
    return context

class PessoaCreate(CreateView):
  model = Pessoa
  fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
  success_url = reverse_lazy('pessoa_list')

class PessoaUpdate(UpdateView):
  model = Pessoa
  fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
  success_url = reverse_lazy('pessoa_list')

class PessoaDelete(DeleteView):
  model = Pessoa
  success_url = reverse_lazy('pessoa_list')

class PessoaBulk(View):
  def get(self, request):
    pessoas = ['João', 'Maria', 'Betina', 'Rafael', 'Frederico', 'Victor']
    lista_pessoas = []

    for pessoa in pessoas:
      p = Pessoa(first_name=pessoa, salary=123, age=2)
      lista_pessoas.append(p)

      Pessoa.objects.bulk_create(lista_pessoas)

    return HttpResponse('Deu bom') 