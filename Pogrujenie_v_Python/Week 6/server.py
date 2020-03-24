import asyncio


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )
    server = loop.run_until_complete(coro)
    try:
        loop.run_forever()
        print('hello')
    except KeyboardInterrupt:
        pass
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


class ClientServerProtocol(asyncio.Protocol):
    storage = {}

    def __init__(self):
        super().__init__()

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = self.process_data(data.decode())
        self.transport.write(resp.encode())

    def process_data(self, data):
        try:
            data_splitted = data.split()
            command = data_splitted[0]
            ret = ''
            if command not in ('get', 'put'):
                return 'error\nwrong command\n\n'
            if len(data_splitted) == 1:
                return 'error\nwrong command\n\n'
            else:
                ret = 'ok\n'
            if command == 'get':
                if len(data_splitted) != 2:
                    return 'error\nwrong command\n\n'
                key = data_splitted[1]
                if key != '*' and key not in ClientServerProtocol.storage:
                    return 'ok\n\n'
                ret += self.get(key)
            elif command == 'put':
                try:
                    value = float(data_splitted[2])
                    timestamp = int(data_splitted[3])
                except:
                    return 'error\nwrong command\n\n'
                if len(data_splitted) != 4:
                    return 'error\nwrong command\n\n'
                metric = data_splitted[1:]
                self.put(metric)
                ret += '\n'
            return ret
        except:
            return 'error\nwrong command\n\n'

    def get(self, key):
        ret = ''
        if key == '*':
            for key, value in ClientServerProtocol.storage.items():
                for v in sorted(value):
                    ret += '%s %s %s\n' % (key, float(value[v]), v)
            ret += '\n'
            return ret
        else:
            values = ClientServerProtocol.storage.get(key)
            if values:
                for v in sorted(values):
                    ret += '%s %s %s\n' % (key, float(values[v]), v)
                ret += '\n'
                return ret
            else:
                return 'ok\n\n'

    def put(self, metric):
        k, v1, v2 = metric
        if k not in ClientServerProtocol.storage:
            ClientServerProtocol.storage[k] = {}
            ClientServerProtocol.storage[k].update({v2: v1})
        else:
            ClientServerProtocol.storage[k].update({v2: v1})


# run_server('127.0.0.1', 8181)
