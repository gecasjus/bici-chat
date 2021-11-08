import socket

class EchoSocket:
    def __init__(self, host='127.0.0.1', port=8000):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))
        self.socket.listen(5)

    def run(self):
        conn, _ = self.socket.accept()

        try:
            while True:
                data = conn.recv(4096)
                if data:
                    print(f'EchoSocket got {data}')
                    self.handle_request(data)
                    conn.sendall(data)
                else:
                    break
        finally:
            conn.close()

    def handle_request(self, data):
        return data 