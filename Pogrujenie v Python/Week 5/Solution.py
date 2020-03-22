import time
import socket


class ClientError(Exception):
    pass


class Client:
    def __init__(self, ip, port, timeout=None):
        self.ip = ip
        self.port = port
        self.timeout = timeout
        self.metric_dict_test = {'palm.cpu': [], 'palm.memory': [],
                            'palm.disk_usage': [], 'palm.network_usage': [],
                            'eardrum.cpu': [], 'eardrum.memory': [],
                            'eardrum.disk_usage': [], 'eardrum.network_usage': []}

    def put(self, metric, value, timestamp=None):
        if timestamp is None:
            timestamp = int(time.time())
        request = 'put {} {} {}\n'.format(metric, value, timestamp).encode()
        with socket.create_connection((self.ip, self.port)) as sock:
            sock.send(request)
            response = sock.recv(1024).decode('utf-8').split('\n')
        try:
            self.metric_dict_test.get(metric).append((value, timestamp))
        except AttributeError:
            pass
        if response[0] != 'ok':
            raise ClientError
    # Пользовательское исключение - ClientError в случае неуспешной отправки

    def get(self, metric):
        metric_dict = dict()
        if metric == '*':
            request = 'get *\n'.encode()
        else:
            request = 'get {}\n'.format(metric).encode()
        with socket.create_connection((self.ip, self.port)) as sock:
            sock.send(request)
            response = sock.recv(1024).decode('utf-8').split('\n')
            # print(response)
            # print(len(response))
        # if ('palm' or 'eardrum') not in metric:
        #     raise ClientError
        if (response[-1] and response[-2]) == '':
            response.remove('')
            response.remove('')
        else:
            raise ClientError
        if response[0] != 'ok':
            raise ClientError
        if response[0] == 'ok' and len(response) == 1:
            return metric_dict
        for _ in range(1, len(response)):
            x = response[_].split(' ')
            try:
                metric_dict[x[0]] = (float(x[1]), int(x[2]))
            except ValueError:
                raise ClientError
            except IndexError:
                raise ClientError
            if len(x) != 3:
                raise ClientError
        return metric_dict
        # if len(response)
        # return self.metric_dict[metric]
    # Пользовательское исключение - ClientError в случае неуспешной отправки
    # Метод get возвращает словарь с метриками (смотрите пример ниже) в случае успешного получения ответа от сервера и
    # выбрасывает исключение ClientError в случае не успешного.


# a = Client('127.0.0.1', 8888)
# a.get('palm.cpu')
# a.put('palm.cpu', 2.5, 2)
# a.put('palm.cpu', 3.0, 5)
# a.put('eardrum.cpu', 4.0, 3453)