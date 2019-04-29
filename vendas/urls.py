from django.urls import path
from .views import DashboardView, NovoPedidoView, NovoItensPedidoView, ListaVendas, EditVenda, DeleteVenda, DeleteItemVenda

urlpatterns = [
  path('dashboard/', DashboardView.as_view(), name='dashboard'),
  path('novo-pedido', NovoPedidoView.as_view(), name='novo_pedido'),
  path('novo-item-pedido/<int:venda>', NovoItensPedidoView.as_view(), name='novo_item_pedido'),
  path('', ListaVendas.as_view(), name='lista_vendas'),
  path('edit-venda/<int:venda>/', EditVenda.as_view(), name='edit_venda'),
  path('delete-venda/<int:venda>', DeleteVenda.as_view(), name='delete_venda'),
  path('delete-item-venda/<int:item>', DeleteItemVenda.as_view(), name='delete_item_confirm')
]