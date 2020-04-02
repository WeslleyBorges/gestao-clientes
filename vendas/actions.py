def mudar_nfe_emitida(modeladmin, request, queryset):
  if request.user.has_perm('vendas.setar_nfe'):
    queryset.update(nfe_emitida=True)


mudar_nfe_emitida.short_description = 'NF-e emitida'


def mudar_nfe_nao_emitida(modeladmin, request, queryset):
  queryset.update(nfe_emitida=False)


mudar_nfe_nao_emitida.short_description = 'NF-e não emitida'
