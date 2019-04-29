from django.contrib import admin
from .models import Pessoa, Documento

class DocumentoAdmin(admin.ModelAdmin):
    search_fields = ['num_doc']

class PessoaAdmin(admin.ModelAdmin):
   fieldsets = (
     ('Dados pessoais', {'fields': ('first_name', 'last_name', 'doc')}),
    ('Dados complementares', {
       'classes': ('collapse',),
       'fields': ('age', 'salary', 'bio')})
)

search_fields = ('first_name', 'last_name')
raw_id_fields = ('doc',)
readonly_fields = ('salary',)

def tem_foto(self, obj):
  if obj.tem_foto:
    return 'Sim'
  return 'Não'

  tem_foto.short_description = 'Possui foto'

  #Agrupamento das tuplas para ficarem na mesma linha do form
  fields = (('first_name', 'last_name'), ('age', 'salary'), 'bio', 'photo')
  
  list_display = ('first_name', 'last_name', 'age', 'salary', 'bio', 'photo')
  list_filter = ('age', 'last_name')

# Register your models here.
admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Documento, DocumentoAdmin)