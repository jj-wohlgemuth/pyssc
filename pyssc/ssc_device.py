import socket
import time
import logging
from .Ssc_transaction import Ssc_transaction


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

    def connect(self, interface: str = "%eth0", port: int = 45):
        self.port = port
        self.socket = socket.create_connection((self.ip + interface, port))
        self.socket.setblocking(True)
        self.socket.settimeout(1)

    def disconnect(self):
        self.socket.close()

    def send_ssc(self,
                 command: str,
                 interface: str = "%eth0",
                 buffersize: int = 512,
                 port: int = 45):
        self.port = port
        request_raw = f'{command}\r\n'.encode('utf-8')
        try:
            self.socket.sendto(request_raw, (self.ip + interface, self.port))
        except Exception as e:
            logging.warning('socket connection closed. Reopening. ' + str(e))
            self.connect(interface=interface, port=port)
            self.socket.sendto(request_raw, (self.ip + interface, self.port))
        data = self.socket.recv(buffersize)
        ssc_transaction = Ssc_transaction()
        ssc_transaction.TX = command
        ssc_transaction.RX = data.decode('utf-8')
        return ssc_transaction
