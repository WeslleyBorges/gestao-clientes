from django.db import models
from django.core.mail import send_mail, mail_admins, send_mass_mail
from django.template.loader import render_to_string

class Documento(models.Model):
  num_doc = models.CharField(max_length=50)

  def __str__(self):
    return self.num_doc


# Create your models here.
class Pessoa(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  age = models.IntegerField()
  salary = models.DecimalField(max_digits=5, decimal_places=2)
  bio = models.TextField()
  photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)
  doc = models.OneToOneField(Documento, null=True, blank=True, on_delete=models.CASCADE)
  
  class Meta:
    permissions = (
      ('visualizar_pessoa_detail', 'Permissão para visualizar as informações de uma pessoa específica.'),
    )

  @property
  def nome_completo(self):
    return self.first_name + ' ' + self.last_name

  def __str__(self):
    return self.first_name + ' ' + self.last_name

  def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

    super(Pessoa, self).save(force_insert=False, force_update=False, using=None,
             update_fields=None)

    clients_emails_root = 'clientes/emails/'

    data = {'cliente': self.first_name}

    plain_text = render_to_string(clients_emails_root + 'novo_cliente.txt', data)
    html_text = render_to_string(clients_emails_root + 'novo_cliente.html', data)
    destination_emails = ['weslleys2fernanda@gmail.com', 'weslleynfs@gmail.com']

    send_mail(
      'Novo cliente cadastrado',
      #'Ó cliente com nome %s acabou de ser cadastrado em nossa base de dados.' % self.first_name,
      plain_text,
      'weslleys2fernanda@gmail.com',
      destination_emails,
      html_message=html_text,
      fail_silently=True,
    )

    mail_admins(
      'Novo cliente %s cadastrado!' % self.first_name,
      plain_text,
      html_message=html_text,
      fail_silently=True,
    )

    message1 = ('Mensagem massiva 1', plain_text, 'weslleys2fernanda@gmail.com', ['weslleys2fernanda@gmail.com'])
    message2 = ('Mensagem massiva 2', html_text, 'weslleys2fernanda@gmail.com', ['weslleys2fernanda@gmail.com'])

    send_mass_mail([message1, message2], fail_silently=True)

