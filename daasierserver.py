import socketserver

import codeParser

class DaaSierHandler(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).strip().decode()
        self.headers = self.data.split('\n')
        self.command = self.headers[0].split(' ')[0]
        self.path = self.headers[0].split(' ')[1]
        print("server.{}('{}')".format(self.command, self.path))

        # Really rather naive routing...
        if self.command.upper() == "GET":
            self.request.sendall('GET world!\n'.encode())
        elif self.command.upper() == "POST":
            # TODO: Parse the data given in the POST and convert to string for function
            self.data = ''
            self.request.sendall("{}\n".format(codeParser.code_to_json(self.data)).encode())
        else:
            self.request.sendall('Server only supports GET and POST!\n'.encode())



if __name__ == "__main__":
    HOST, PORT = "localhost", 8080
    server = socketserver.TCPServer((HOST, PORT), DaaSierHandler)
    server.serve_forever()
