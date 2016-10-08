#!/usr/bin/python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import subprocess
import json
import httplib

flag = 0

def request():
  httpServDst = httplib.HTTPConnection("127.0.0.1", 10369)
  httpServDst.connect()

  httpServDst.request('POST', '/cgi_form.cgi', '{"name":"Stream"}')
  response = httpServDst.getresponse()
  httpServDst.close()
  return

print "Request"
request()






