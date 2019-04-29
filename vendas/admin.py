from django.contrib import admin
from .models import Venda, ItensPedido

class ItensPedidoInline(admin.TabularInline):
  model = ItensPedido
  extra = 2

# Register your models here.
class VendaAdmin(admin.ModelAdmin):
  list_filter = ('pessoa__doc',)
  list_display = ('id', 'numero', 'pessoa', 'nfe_emitida',)  
  #fieldsets = (('Itens', {'fields': ('produto',)}),)

  readonly_fields = ('valor',)

  inlines = [ItensPedidoInline]

  def total_vendas(self, obj):
    return obj.get_total_vendas()

  total_vendas.short_description = 'Total'

  actions = []

admin.site.register(Venda, VendaAdmin)
admin.site.register(ItensPedido)