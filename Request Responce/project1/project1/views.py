from django.http import HttpResponse

def home(request):
    print(request)
    return HttpResponse("this is the fisrt time in django")

