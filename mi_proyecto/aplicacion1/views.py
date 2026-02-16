from django.http import HttpResponse

# Create your views here.
def vista_ejemplo(request):
    return HttpResponse("¡Hola mundo!")