from django.forms import ModelForm
from .models import Pessoa

class PessoaForm(ModelForm):
  class Meta:
    model = Pessoa
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']