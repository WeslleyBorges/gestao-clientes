from django.urls import path, include
from .views import lista_pessoas
from .views import nova_pessoa
from .views import atualizar_pessoa
from .views import deletar_pessoa
from home import urls as home_urls
from .views import ListaPessoas, PessoaDetail, PessoaCreate, PessoaUpdate, PessoaDelete, PessoaBulk

urlpatterns = [
    path('lista-pessoas/', lista_pessoas, name='lista_pessoas'),
    path('nova-pessoa/', nova_pessoa, name='nova_pessoa'),
    path('atualizar-pessoa/<int:id>/', atualizar_pessoa, 
          name='atualizar_pessoa'),
    path('deletar-pessoa/<int:id>/', deletar_pessoa, 
          name='deletar_pessoa'),
    path('', include(home_urls), name='logout'),
    path('pessoa_list/', ListaPessoas.as_view(), name='pessoa_list'),
    path('pessoa_detail/<int:pk>', PessoaDetail.as_view(), name='pessoa_detail'),
    path('pessoa_update/<int:pk>', PessoaUpdate.as_view(), name='pessoa_update'),
    path('pessoa_create/', PessoaCreate.as_view(), name='pessoa_create'),
    path('pessoa_delete/<int:pk>', PessoaDelete.as_view(), name='pessoa_delete'),
      path('pessoa_bulk/', PessoaBulk.as_view(), name='pessoa_bulk'),
]
