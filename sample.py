#!/usr/bin/env python
#
import sys
import json
import httplib
import contextlib
import urlparse
import base64
import datetime
import os

def smileface(image):
    url="http://face.baidu.com/faceprop/xiaolian"
    ret = send_post(url,'CalcFaceAPI',image)
    return ret

def test_xiaolian(act):
    url="http://face.baidu.com/faceprop/xiaolian"
    #url="http://10.46.123.59:8090/faceprop/xiaolian"
    test_method(url,act) 

def test_method(url,act):
    img=None
    if('CalcFaceAPI' in act):
        img = open('./renlian.jpg', 'rb') 
        tim,ret=send_post(url,'CalcFaceAPI',img) 
        print 'CalcFaceAPI',ret 
def send_post(url,method,img):
    print img
    address = urlparse.urlparse(url)
    req = json.dumps({
        'jsonrpc': '2.0',
        'method': method,
        'params': [{
		'type': 'faceapi',
		'appid': '10000',
		'encoding': 1,
		'fromdevice': 'pc/android/ios',
        'clientip': '10.92.132.48',
		'calcType': 267,
	    	'image':img
        }],
	'id':12345
    })

    headers = {
        # 'Content-Length': str(len(req)),
        'Content-Length': str(len(req)),
        'Accept': 'text/plain'
    }
    tmStart = int(datetime.datetime.now().second * 1000 + datetime.datetime.now().microsecond / 1000)
    ret={}
    for n in range (0, 1, 1):
        with contextlib.closing(httplib.HTTPConnection(address.netloc)) as c:
            c.request('POST', address.path, req, headers)
            tmp=c.getresponse().read()
            resp = json.loads(tmp)
            if 'error' not in resp:
                if resp.has_key('result') and resp['result'].has_key('_ret'):
                    tmp=resp['result']['_ret']['jsonRet']
                    resp = json.loads(tmp)
                    ret=json.dumps(resp,encoding='UTF-8', sort_keys=True, indent=2)
                else:
                    ret=json.dumps(resp,encoding='UTF-8', sort_keys=True, indent=2)
                    #print 'success: %s' % json.dumps(resp['result'], encoding='UTF-8', ensure_ascii=False )
            else:
                print 'fail with %d: %s' % (resp['error']['code'], resp['error']['message'])
    tmEnd = int(datetime.datetime.now().second * 1000 + datetime.datetime.now().microsecond / 1000) 
    tim=tmEnd - tmStart
    return ret


if __name__ == '__main__':
    test_xiaolian({'CalcFaceAPI'})

