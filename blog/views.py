from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog(request):
    print("Fazer outras coisas aqui")
    return HttpResponse("Uma mensagem de retorno: Blog")