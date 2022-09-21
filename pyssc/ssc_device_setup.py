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

    def add_device(self, ssc_device):
        self.ssc_devices.append(ssc_device)

    def remove_device(self, ssc_device):
        self.ssc_devices.remove(ssc_device)

    def connect_all(self):
        for ssc_device in self.ssc_devices:
            ssc_device.connect()

    def send_all(self, command, interface):
        for ssc_device in self.ssc_devices:
            ssc_device.send_ssc(command, interface=interface)

    def disconnect_all(self):
        for ssc_device in self.ssc_devices:
            ssc_device.disconnect()

    def from_json(self, json_path):
        with open(json_path) as json_file:
            setup_dict = json.load(json_file)
        self.__init__([])
        for device in setup_dict:
            self.add_device(Ssc_device(device, setup_dict[device]))
        pass

    def to_json(self, json_path):
        setup_dict = {}
        for device in self.ssc_devices:
            setup_dict[device.name] = device.ip
        with open(json_path, "w") as json_file:
            json.dump(setup_dict, json_file)
