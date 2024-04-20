from django.http import HttpResponse

def v1(request):
    data="<h1 style='color : red'>Hello This is My First Response</h1>"
    return HttpResponse(data)