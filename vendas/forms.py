from django import forms

class ItensPedidoForm(forms.Form):
  produto_id = forms.CharField(label='ID do Produto', max_length=1000)
  quantidade = forms.FloatField(label='Quantidade')
  desconto = forms.DecimalField(label='Desconto', max_digits=7, decimal_places=2)