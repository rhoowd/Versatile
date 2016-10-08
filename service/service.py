#!/usr/bin/python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import subprocess
import json

flag = 0
class MyHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    if self.path == '/favicon.ico':
      return

    print self.path

    self.send_response(200)

    self.send_header("Content-type", "text/html")
    self.end_headers()

    self.wfile.write('<h1>Hello world</h1>')
    self.wfile.write('<h2 style="color:green">Welcome!</h2>')

  def do_POST(self):
    print 'headers:', self.headers
    length = int(self.headers['Content-Length'])
    data = self.rfile.read(length).decode('utf-8')
    json_msg = json.loads(str(data))
    print json_msg
    if json_msg['name'] == "src":
      print "src"
      self.send_response(200)
      subprocess.Popen(['./src.sh'])
      # localhost:xxxx/update
      return
    elif json_msg['name'] == "dst":
      print "dst"
      self.send_response(200)
      subprocess.Popen(['./dst.sh'])
      # localhost:xxxx/update
      return
    self.send_response(200)


PORT = 10369

try:
  server = HTTPServer(('', PORT), MyHandler)
  print('Start server. port:', PORT)
  server.serve_forever()

except KeyboardInterrupt:
  print('^C received, shutting down the web server')
  server.socket.close()