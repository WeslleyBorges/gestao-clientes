from django.urls import path
from .views import DashboardView, NovoPedidoView, NovoItensPedidoView

urlpatterns = [
  path('dashboard/', DashboardView.as_view(), name='dashboard'),
  path('novo-pedido', NovoPedidoView.as_view(), name='novo_pedido'),
  path('novo-item-pedido/<int:venda>', NovoItensPedidoView.as_view(), name='novo_item_pedido')
]