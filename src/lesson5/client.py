import socket
import time


class ClientError(BaseException):
    def __init__(self, message):
        super().__init__(message)


class Client:
    def __init__(self, host, port, **kwargs):
        self.sock = socket.create_connection((host, port))
        self.timeout = kwargs.get('timeout', None)

    def put(self, key, value, timestamp=str(int(time.time()))):
        self.sock.sendall(
            'put {key} {value} {timestamp}\n'.format(key=key, value=value, timestamp=timestamp).encode('ascii')
        )
        response = self.sock.recv(100000)

        if 'ok' not in response.decode().split('\n'):
            raise ClientError(response)

    def get(self, key):
        self.sock.sendall('get {key}\n'.format(key=key).encode('ascii'))
        r = self.sock.recv(100000).decode().split('\n')

        if 'ok' not in r:
            raise ClientError(r)

        response = list(filter(lambda x: x != 'ok' and x != '', r))

        splited = list(map(lambda x: x.split(' '), response))
        result_map = {}

        for item in splited:
            value = (int(item[2]), float(item[1]))

            if item[0] in result_map.keys():
                result_map.update({item[0]: result_map.get(item[0]) + [value]})
            else:
                result_map.update({item[0]: [value]})

        return result_map

