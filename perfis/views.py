from django.shortcuts import render
from perfis.models import Perfil

def index(request):
	return render(request, 'index.html')

def exibir(request, perfil_id):
    # if perfil_id == '2':
    # 	perfil = Perfil('Isabela Climaco', 'isabelasclimaco@gmail.com', '98172-6597', 'fga')
    perfil = Perfil.objects.get(id=perfil_id)
    return render(request, 'perfil.html', {"perfil" : perfil})