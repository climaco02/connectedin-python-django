from django.shortcuts import render
from perfis.models import Perfil

def index(request):
	return render(request, 'index.html')

def exibir(request, perfil_id):
    print 'ID do perfil recebido: %s' % (perfil_id)

    perfil = Perfil()

    if perfil_id == '1':
    	perfil = Perfil('Gabriel Climaco', 'gabrielsclimaco@gmail.com', '99293-2523', 'fga')

    if perfil_id == '2':
    	perfil = Perfil('Isabela Climaco', 'isabelasclimaco@gmail.com', '98172-6597', 'fga')

    return render(request, 'perfil.html', {"perfil" : perfil})