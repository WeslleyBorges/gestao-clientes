from django.shortcuts import render
from django.views import View 
from .models import Venda, ItensPedido
from django.http import HttpResponse
from .forms import ItensPedidoForm

# Create your views here.
class DashboardView(View):

  def dispatch(self, request, *args, **kwargs):
    if not request.user.has_perm('ver_dashboard'):
      return HttpResponse('<h1>Acesso negado</h1>')
    return super(DashboardView, self).dispatch(request, *args, **kwargs)

  def get(self, request): 
    data = {}
    data['media'] = Venda.objects.media()
    data['maximo'] = Venda.objects.maximo()
    data['minimo'] = Venda.objects.minimo()
    data['count'] = Venda.objects.count()
    data['nfe'] = Venda.objects.nfe_emitida_count()
    data['info_vendas'] = Venda.objects.info_vendas()

    return render(request, 'vendas/dashboard.html', data)

class NovoPedidoView(View):
  def get(self, request):
    return render(request, 'vendas/novo-pedido.html')

  def post(self, request):

    data_dict = {}
    data_dict['numero'] = request.POST['num_venda']
    data_dict['desconto'] = request.POST['desconto']
    #data_dict['venda'] = request.POST['venda_id']

    numero_venda = request.POST['num_venda']

    venda = Venda.objects.get(numero=numero_venda)

    #TODO: Refatorar essa parte depois. Tá uma tremenda zona, isso aqui. Não quero perder tempo agora. Refatoro ao pegar o código para brincar em casa.

    if not venda.id:
      venda = Venda.objects.create(
        numero = data_dict['numero'],
        desconto = float(data_dict['desconto'])
      )

    itens = venda.itenspedido_set.all()
    data_dict['venda_obj'] = venda
    data_dict['itens'] = itens

    return render(request, 'vendas/novo-pedido.html', data_dict)

class NovoItensPedidoView(View):

  def get(self, request, pk):
    pass

  def post(self, request, venda):
    data = {}

    item_pedido = ItensPedido.objects.create(

      produto_id=request.POST['produto_id'], quantidade=request.POST['quantidade'],
      desconto = request.POST['desconto'], venda_id=venda
    )

    data['form_item'] = ItensPedidoForm()
    data['numero'] = item_pedido.venda.numero
    data['desconto'] = item_pedido.venda.desconto
    data['venda'] = item_pedido.venda.id
    data['venda_obj'] = item_pedido.venda
    data['itens'] = item_pedido.venda.itenspedido_set.all()

    return render(request, 'vendas/novo-pedido.html', data)