import json
from .ssc_device import Ssc_device


class Ssc_device_setup():
    """
    :param

    .. code-block:: python
        :caption: Todo

        >>> Todo

    """
    def __init__(self, ssc_devices: list = []):
        self.ssc_devices = ssc_devices

    def add_device(self, ssc_device: Ssc_device):
        self.ssc_devices.append(ssc_device)

    def remove_device(self, ssc_device: Ssc_device):
        self.ssc_devices.remove(ssc_device)

    def connect_all(self, interface: str = "%eth0", port: int = 45, timeout: int = 4):
        for ssc_device in self.ssc_devices:
            ssc_device.connect(interface=interface, port=port, timeout=timeout)

    def send_all(self,
                 command: str,
                 interface: str = "%eth0",
                 buffersize: int = 512,
                 port: int = 45):
        for ssc_device in self.ssc_devices:
            ssc_device.send_ssc(command,
                                interface,
                                buffersize,
                                port)

    def disconnect_all(self):
        for ssc_device in self.ssc_devices:
            ssc_device.disconnect()

    def from_json(self, json_path: str):
        with open(json_path) as json_file:
            setup_dict = json.load(json_file)
        self.__init__([])
        for device in setup_dict:
            self.add_device(Ssc_device(device, setup_dict[device]))

    def to_json(self, json_path: str):
        setup_dict = {}
        for device in self.ssc_devices:
            setup_dict[device.name] = device.ip
        with open(json_path, "w") as json_file:
            json.dump(setup_dict, json_file)
