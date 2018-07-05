from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
#URL access with parameter named msg
#def index(request):
#	if "msg" in request.GET:
#		msg = request.GET['msg']
#		result = "You Typed: " + msg + "."
#	else:
#		result = "Parameters are missing"
#
#	return HttpResponse(result)

#def index(request, id, nickname):
#    #recieve http://localhost:8000/hello/123/kaya/
#    result = "Your ID: " + str(id) + " Name: " + str(nickname)
#    return HttpResponse(result)

def index(request):
    #return render(request, 'hello/index.html')
    return render(request, 'hello_temp/index.html')
