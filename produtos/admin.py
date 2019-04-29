from django.contrib import admin
from .models import Produto

# Register your models here.
class ProdutoAdmin(admin.ModelAdmin):
  fieldsets = (
    ('Descricao', {'fields': ('descricao',)}),
    ('Preco', {'fields': ('preco',)})
  )

admin.site.register(Produto, ProdutoAdmin)