from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os

#-INFO- JSON databse file location
database_file = 'api/data.json'

#-INFO- Check if database exsist and if it doesnt add it
if not os.path.exists(database_file):
    with open(database_file, 'w') as f:
        json.dump([], f)

#********************************************************#
#* Custom RequestHandler Class *#  
#********************************************************#
class RequestHandler(BaseHTTPRequestHandler):

    #-INFO- ::FUNCTION:: GET routing
    def do_GET(self):
        if self.path == '/api':
            with open(database_file, 'r') as f:
                data = json.load(f)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
    
    #-INFO- ::FUNCTION:: POST routing
    def do_POST(self):
        if self.path == '/api':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')

            try:
                post_data = json.loads(post_data)
            except json.JSONDecodeError:
                self.send_response(400)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'Invalid JSON data')
                return

            with open(database_file, 'r') as f:
                data = json.load(f)
            
            key = len(data) + 1
            data[key] = post_data

            with open(database_file, 'w') as f:
                json.dump(data, f, indent=4)
            
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"id": key}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    #-INFO- ::FUNCTION:: DELETE Routing
    def do_DELETE(self):
        if self.path.startswith('/api/'):
            key = self.path.split('/')[-1]

            with open(database_file, 'r') as f:
                data = json.load(f)

            if key in data:
                deleted_item = data.pop(key)

                with open(database_file, 'w') as f:
                    json.dump(data, f, indent=4)

                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"message": "Data deleted successfully"}).encode('utf-8'))
            else:
                print(f"Key {key} not found in data:", data)
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"message": "Data not found"}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

#-INFO- ::FUNCTION:: Main run function for server
def main(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server localhost on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    main()