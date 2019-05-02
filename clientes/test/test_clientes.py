from django.test import TestCase
from clientes.models import Pessoa

# Lembrar de criar um Python Package para colocar os arquivos de teste dentro,
# pois este conterá o __init__.py dentro

class ClienteTestCase(TestCase):
    def setUp(self):
        self.pessoa = Pessoa.objects.create(age=22, salary=123)

    def test_criar_pessoa(self):
        msg = 'Deu beyblade!'
        self.assertTrue(Pessoa.objects.count() > 0, msg)