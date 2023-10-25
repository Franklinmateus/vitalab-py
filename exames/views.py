from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import TiposExames, PedidosExame
from datetime import datetime

@login_required
def solicitar_exames(request):
    tipos_exames = TiposExames.objects.all()  
    if request.method == "GET":
        return render (request, 'solicitar_exames.html', {'tipos_exames': tipos_exames})
    else:
        exames_id = request.POST.getlist('exames')
        
        solicitacao_exames = TiposExames.objects.filter(id__in=exames_id)
        #preco_total = solicitacao_exames.aggregate(total=Sum('preco'))['total]
        preco_total = 0
        for i in solicitacao_exames:
            if i.disponivel:
                preco_total += i.preco

        return render (request, 'solicitar_exames.html', {'solicitacao_exames': solicitacao_exames, 'preco_total': preco_total, 'tipos_exames': tipos_exames})

def fechar_pedido(request):
    exames_id = request.POST.getlist('exames')
    
    pedido_exame = PedidosExame(
        usuario=request.user,
        data = datetime.now()
    )
    
    pedido_exame.save()
    
    return HttpResponse("estou aq")