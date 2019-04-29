from django import template
import datetime

register = template.Library()

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)

@register.simple_tag
def footer_message():
  return 'Desenvolvimento com Jungle 2.2'