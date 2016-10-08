#!/usr/bin/python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import subprocess
import json
import time
import httplib

flag = 0

stream_src = "10.10.0.2"
stream_dst = "10.10.0.3"

# stream_src = "127.0.0.1"
# stream_dst = "127.0.0.1"

def request():
  httpServDst = httplib.HTTPConnection(stream_src, 10369)
  httpServDst.connect()

  httpServDst.request('POST', '/cgi_form.cgi', '{"name":"src"}')
  response = httpServDst.getresponse()
  httpServDst.close()

  time.sleep(1)

  httpServDst = httplib.HTTPConnection(stream_dst, 10369)
  httpServDst.connect()

  httpServDst.request('POST', '/cgi_form.cgi', '{"name":"dst"}')
  response = httpServDst.getresponse()
  httpServDst.close()

  return

print "Request"
request()






