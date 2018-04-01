import asyncio
import json
from functools import reduce

cache = {}


def new_line():
    return '\n'


def all_data():
    return 'ok\n' + json.dumps(cache)


def data_by_key(data, key):
    return 'ok\n' + json.dumps({key: data})


def process_data(data):
    prepared = data.replace('\r\n', '').split(' ')
    method = prepared[0]
    key = prepared[1]

    if method != 'get' and method != 'put' or key == '':
        return 'error\nwrong command\n\n'

    if method == 'put':
        value = cache.get(key, None)

        if key in cache.keys():
            cache.update({key: value + [(prepared[2], prepared[3])]})
        else:
            cache.update({key: [(prepared[2], prepared[3])]})

    if method == 'get':
        if key == '*':
            return all_data()

        value = cache.get(key, None)

        if key not in cache.keys():
            return 'ok\n\n'
        else:
            return data_by_key(value, key)

    return 'ok\n\n'


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )

    server = loop.run_until_complete(coro)
    print('Server started at: ', '{host}: {port}'.format(host=host, port=port))

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = process_data(data.decode())
        self.transport.write(resp.encode())

