# Create your views here.
import json
from django.http import HttpResponse

def get_proxy_url(code):
    if code == 'GR':
        return "150.140.184.110:3128"
    elif code == 'US':
        return "72.64.146.136:8080"
    elif code == 'UK':
        return "109.75.171.216:6515"
    
def get_countries(req):
    if req.method == "GET":
        return HttpResponse(json.dumps([
            {"code":"XX","name":"Deactivate","img_url":"icon.png"},
            {"code":"GR","name":"Greece","img_url":"http://yuba.stanford.edu/~yiannis/greece.png"},
            {"code":"US","name":"United States","img_url":"http://yuba.stanford.edu/~yiannis/us.png"},
            {"code":"UK","name":"United Kingdom","img_url":"http://yuba.stanford.edu/~yiannis/uk.png"},
            ]))

def get_country(req):
    if req.method == "GET":
        code = req.GET.get('code','')
        proxy_url = get_proxy_url(code)
        url,port = proxy_url.split(':')
        port = int(port)
        return HttpResponse(json.dumps({"code":code,"proxy_url":url,"proxy_port":port}))
