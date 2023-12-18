from django.shortcuts import render
from django.http import HttpResponse
import socket
# Create your views here.


def home(request):
    return render(request,"home.html", {'names': 'dev'})

def check(request):
    name = request.GET.get('name', '')
    ipaddress = request.GET.get('ipaddress', '')
    print ("ipaddress", ipaddress )
    try :
 #      (type(name)==str )
        hostname = socket.gethostbyaddr(ipaddress)[0]
        print (f"the host name is {hostname}")
        output = f"Welcome {name}! Hostname: {hostname}"
        return render(request,"result.html", {'result' : output})
    except Exception as e:
        print ("Plese enter a string")
        print (e)
        return render(request, "result.html", {'result': "Error: An unexpected error occurred."})
    finally:
        print ("closed")


