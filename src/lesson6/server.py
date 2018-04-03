import asyncio
from functools import reduce


cache = {}


def new_line():
    return '\n'


def all_data():
    return reduce(
        lambda acc, key: f'{acc}{new_line().join(list(map(lambda x: f"{key} {x[1]} {x[0]}", cache.get(key))))}\n',
        cache.keys(),
        'ok\n'
    )


def data_by_key(key):
    return reduce(
        lambda acc, item: f'{acc}{key} {item[1]} {item[0]}\n',
        cache.get(key),
        'ok\n'
    )


def value_by_key(key, timestamp, val):
    value = cache.get(key, None)
    if key in cache.keys():
        return value if any(f[0] == timestamp for f in value) else value + [(timestamp, val)]
    else:
        return [(timestamp, val)]


def process_data(data):
    prepared = data.replace('\r\n', '').split(' ')
    method = prepared[0]
    key = prepared[1].replace('\n', '')

    if method != 'get' and method != 'put' or key == '':
        return 'error\nwrong command\n\n'

    if method == 'put':
        val = float(prepared[2])
        timestamp = int(prepared[3])

        cache.update({key: value_by_key(key, timestamp, val)})

    if method == 'get':
        if key == '*':
            return all_data() + '\n'

        if key not in cache.keys():
            return 'ok\n\n'
        else:
            return data_by_key(key) + '\n'

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


# run_server('127.0.0.1', 8888)
