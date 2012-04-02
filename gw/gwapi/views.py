# Create your views here.
import json
from django.http import HttpResponse

def get_proxy_url(code):
    if code == 'GR':
        return "193.46.60.74:3128"
    elif code == 'US':
        return "148.52.151.3:3128"
    elif code == 'UK':
        return "149.52.151.3:3128"
    
def get_countries(req):
    if req.method == "GET":
        return HttpResponse(json.dumps([{"code":"GR","name":"Greece","img_url":"http://yuba.stanford.edu/~yiannis/greece.png"},
                                        {"code":"US","name":"United States","img_url":"http://yuba.stanford.edu/~yiannis/us.png"},
                                        {"code":"UK","name":"United Kingdom","img_url":"http://yuba.stanford.edu/~yiannis/uk.png"},
                                        ]))

def get_country(req):
    if req.method == "GET":
        code = req.GET.get('code','')
        proxy_url = get_proxy_url(code)
        url,port = proxy_url.split(':')
        port = int(port)
        #return HttpResponse("ok")
        return HttpResponse(json.dumps({"code":code,"proxy_url":url,"proxy_port":port}))
