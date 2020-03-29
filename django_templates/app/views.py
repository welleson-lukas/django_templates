from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html',{'cards':card_home})

card_home = {
    "1":{"titulo":"Como governos estão usando dados de localização dos celulares no combate à Covid-19", "descricao":"Tecnologia tem sido abraçada em vários países, incluindo o Brasil; entenda como ela é usada e suas implicações"},
    "2":{"titulo":"De olho no futuro, Airbus apresenta modelo de avião com asas integradas","descricao":"Protótipo Maveric tem fuselagem integrada e não conta com janelas; segundo empresa, modelo consome 20% a menos de combustíveis "},
    "3":{"titulo":"Você sabe o que é o doping tecnológico?","descricao":"Super tênis que aumenta a performance da corrida em 4% trouxe à tona o debate sobre o doping tecnológico"}
}

def sobre(request):
    return HttpResponse("Pagina sobre")

def contato(request):
    return HttpResponse("Pagina contato")