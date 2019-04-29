from django.db import models
from clientes.models import Pessoa
from produtos.models import Produto
from django.db.models import Sum, F, FloatField, Max
from django.db.models.signals import post_save
from django.dispatch import receiver
from .managers import VendaManager
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class Venda(models.Model):
  numero = models.CharField(max_length=30)
  valor = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
  desconto = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0)
  impostos = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0)
  pessoa = models.ForeignKey(Pessoa, null=True, blank=True, on_delete=models.PROTECT)
  nfe_emitida = models.BooleanField(default=False)

  def calcular_total(self):
    total = self.itenspedido_set.all().aggregate(
      total_pedido=Sum((F('quantidade') * F('produto__preco')) - F('desconto'), output_field=FloatField())
    )['total_pedido'] or 0

    total = total - (float(self.desconto) - float(self.impostos))
    self.valor = total
    Venda.objects.filter(id=self.id).update(valor=total)

  # Só parou de dizer 'Manager' object has no attribute 'maximo'/'media'/...
  # quando defini o manager de Venda (objects) como 'VendaManager'
  objects = VendaManager()

  class Meta:
    permissions = (
      ('setar_nfe', 'Parâmetro para definir se o usuário está apto a algo relacionado a NF-e'),
      ('Permissão Dois', 'A segunda permissão para algo'),
      ('Permissão Três', 'A terceira permissão para algo'),
      ('ver_dashboard', 'Acesso para visualizar o dashboard de vendas.')
    )

  def __str__(self):
    return self.numero

class ItensPedido(models.Model):
  venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
  produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
  quantidade = models.FloatField()
  desconto = models.DecimalField(max_digits=5, decimal_places=2)

  def __str__(self):
    return str(self.venda) + ' - ' + str(self.produto)

@receiver(post_save, sender=ItensPedido)
def update_vendas_total_itempedido(sender, instance, **kwargs):
  instance.venda.calcular_total()

@receiver(post_save, sender=Venda)
def update_vendas_total_venda(sender, instance, **kwargs):
  instance.calcular_total()