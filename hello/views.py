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

#def index(request):
    #return render(request, 'hello/index.html')
#    return render(request, 'hello_temp/index.html')

def index(request):
    params = {
        "title" : "Hello Index",
        "msg" : "This is a sample page redering in index function",
        "goto" : "next"
    }
    return render(request, 'hello_temp/index.html', params)

def next(request):
    params = {
        'title': "Hello/Next",
        'msg': "this is the next page.",
        'goto': "index"
    }
    return render(request, 'hello_temp/index.html', params)

def form(request):
    msg = request.POST['msg']
    params = {
        'title' : "Hello/From",
        'msg' : "Hello " + msg + " ! "
    }
    return render(request, 'hello_temp/index.html', params)
