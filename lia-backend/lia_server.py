#!/usr/bin/env python
import lib.web as web
import json

def get_proxy_url(code):
    if code == 'GR':
        return "150.140.184.110:3128"
    elif code == 'US':
        return "72.64.146.136:8080"
    elif code == 'UK':
        return "109.75.171.216:6515"

class get_countries():
    def GET(self):
        return json.dumps([
            {"code":"XX","name":"Deactivate","img_url":"images/icon.png"},
            {"code":"GR","name":"Greece","img_url":"images/greece.png"},
            {"code":"US","name":"United States","img_url":"images/us.png"},
            {"code":"UK","name":"United Kingdom","img_url":"images/uk.png"},
            ])

class get_country():
    def GET(self):
        vars = web.input(name = 'web')
        code = web.websafe(vars.code)
        proxy_url = get_proxy_url(code)
        url,port = proxy_url.split(':')
        port = int(port)
        return json.dumps({"code":code,"proxy_url":url,"proxy_port":port})

urls = (
    '/gw/get_countries','get_countries',
    '/gw/get_country', 'get_country')

app = web.application(urls,globals())

if __name__ == '__main__':
    app.run()
