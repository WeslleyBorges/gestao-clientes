from django import template

register = template.Library()

@register.filter
def arredonda(valor, casas_decimais):
  return round(valor, casas_decimais)

