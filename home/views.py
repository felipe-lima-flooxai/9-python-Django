from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    print("Fazer outras coisas aqui")
    return HttpResponse("Uma mensagem de retorno: Home")

