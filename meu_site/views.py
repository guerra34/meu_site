from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Olá mundo! Meu primeiro site com Django está funcionando! 🚀</h1>")
    