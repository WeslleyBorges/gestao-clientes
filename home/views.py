from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import logout
from django.views.generic.base import TemplateView, View
from django.http import HttpResponse

# Create your views here.
#TODO: Refatorar para utilizar threads assim que possível
def home(request):
  return render(request, 'home.html')

#FIXME: Corrigir bug do logout, caso haja
def my_logout(request):
  logout(request)
  return redirect('home')

class HomePageView(TemplateView):
  template_name = 'home2.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    #context['minha_variavel'] = 'Help me T_T'

    primeiro_acesso = self.request.session.get('primeiro_acesso', False)

    if not primeiro_acesso:
      context['message'] = 'Seja bem-vindo ao teu primeiro acesso'
      self.request.session['primeiro_acesso'] = True
    else:
      context['message'] = 'Tu já acessou esta aplicação hoje.'

    return context

class MyView(View):

  def get(self, request, *args, **kwargs):
    #return HttpResponse('Hello, world!')
    #return render(request, 'home3.html')
    response = render_to_response('home3.html')
    response.set_cookie('cookey', 'Alguma coisa relacionada ao valor do cookie.', max_age=60)
    meu_cookie = request.COOKIES.get('cookey')
    print(meu_cookie)
    return response

  def post(self, request, *args, **kwargs):
    return HttpResponse('POST')