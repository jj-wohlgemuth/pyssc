import socket
import time
import logging
from .ssc_transaction import Ssc_transaction


class Ssc_device():
    """
    :param name: device name
    :param ip: ip address of ssc device

    .. code-block:: python
        :caption: todo

        >>> todo

    """
    def __init__(self,
                 name: str,
                 ip: str = None,
                 port: int = 45):
        self.name = name
        self.ip = ip
        self.socket = None
        self.port = port
        self.connected = False
        self.error = ""

    def connect(self, interface: str = "%eth0", port: int = 45, timeout: int=4):
        self.port = port
        self.socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        self.socket.setblocking(True)
        self.socket.settimeout(timeout)
        sock_addr = socket.getaddrinfo(self.ip + interface, port, socket.AF_INET6, proto=6)[0][4]
        try:
          self.socket.connect(sock_addr)
        except socket.error as err:
          self.connected =  False
          self.error = err
          return False

        self.connected = True
        return True


    def disconnect(self):
        self.socket.close()
        self.connected = False

    def send_ssc(self,
                 command: str,
                 interface: str = "%eth0",
                 buffersize: int = 512,
                 port: int = 45):
        self.port = port
        if not self.connected:
            return False

        request_raw = f'{command}\r\n'.encode('utf-8')
        try:
            self.socket.sendto(request_raw, (self.ip + interface, self.port))
        except Exception as e:
            self.connected = False
            self.error = str(e)
            return False

        try:
            data = self.socket.recv(buffersize)
        except Exception as e:
            self.connected = False
            self.error = str(e)
            return False

        ssc_transaction = Ssc_transaction()
        ssc_transaction.TX = command
        ssc_transaction.RX = data.decode('utf-8')
        return ssc_transaction
