from django.db.models import Sum, Max, Min, Count, Avg
from django.db import models

class VendaManager(models.Manager):
  def media(self):
    return '{:.2f}'.format(self.all().aggregate(Avg('valor'))['valor__avg'])
  
  def maximo(self): 
    return '{:.2f}'.format(self.all().aggregate(Max('valor'))['valor__max'])
    
  def minimo(self):
    return self.all().aggregate(Min('valor'))['valor__min']

  def count(self):
    return self.all().aggregate(Count('valor'))['valor__count']
   
  def nfe_emitida_count(self):
    return self.filter(nfe_emitida=True).aggregate(Count('id'))['id__count']

  def info_vendas(self):
    return self.all()