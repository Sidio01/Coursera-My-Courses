import asyncio
from collections import defaultdict


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
    storage = defaultdict(set)
    timestamp_dict = defaultdict(set)

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
                    return 'error\nwrong command\n\n'
                ret += self.get(key)
            elif command == 'put':
                try:
                    value = float(data_splitted[2])
                    timestamp = int(data_splitted[3])
                except ValueError:
                    return 'error\nwrong command\n\n'
                if len(data_splitted) != 4:
                    return 'error\nwrong command\n\n'
                metric = data_splitted[1:]
                self.put(metric)
                ret += '\n'

            return ret

        except IndexError:
            return 'error\nwrong command\n\n'

    def get(self, key):
        ret = ''
        if key == '*':
            for k, values in ClientServerProtocol.storage.items():
                for v1, v2 in values:
                    ret += '{} {} {}\n'.format(k, str(float(v1)), v2)
            ret += '\n'

        else:
            retl = [' '.join([key, str(float(v1)), v2]) + '\n' for (v1, v2) in ClientServerProtocol.storage[key]]
            ret = ''.join(retl) + '\n'
        return ret

    def put(self, metric):
        k, v1, v2 = metric
        try:
            if v2 not in ClientServerProtocol.timestamp_dict[k]:
                ClientServerProtocol.storage[k].add((v1, v2))
                ClientServerProtocol.timestamp_dict[k].add(v2)
            else:
                for _ in ClientServerProtocol.storage[k]:
                    if v2 == _[1]:
                        ClientServerProtocol.storage[k].remove(_)
                        break
                ClientServerProtocol.storage[k].add((v1, v2))
            # print(ClientServerProtocol.storage)
            # print(ClientServerProtocol.timestamp_dict)
        except KeyError:
            ClientServerProtocol.storage[k].add((v1, v2))
            ClientServerProtocol.timestamp_dict[k] = set(v2)


run_server('127.0.0.1', 8181)
