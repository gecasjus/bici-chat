from helpers import EchoSocket

class HTTPServer(EchoSocket):
    def handle_request(self, data):
        return b"Request received!" # send bytes, not string

if __name__ == '__main__':
    server = HTTPServer()
    server.run()