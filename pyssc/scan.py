import time
from zeroconf import IPVersion, ServiceBrowser,\
                     ServiceStateChange, Zeroconf, ZeroconfServiceTypes
from .ssc_device import Ssc_device
from .ssc_device_setup import Ssc_device_setup

found_kh_devices = []
ssc_device_setup = None


def __on_service_state_change(zeroconf: Zeroconf,
                              service_type: str,
                              name: str,
                              state_change: ServiceStateChange) -> None:
    if state_change is ServiceStateChange.Added:
        info = zeroconf.get_service_info(service_type, name)
        if info:
            if info.type == '_ssc._tcp.local.':
                address = info.parsed_addresses()[0]
                name = info.name.replace('._ssc._tcp.local.', '')
                found_kh_devices.append(Ssc_device(name, address))
    global ssc_device_setup
    ssc_device_setup = Ssc_device_setup(found_kh_devices)


def scan(scan_time_seconds=1) -> Ssc_device_setup:
    zeroconf = Zeroconf(ip_version=IPVersion.V6Only)
    services = list(ZeroconfServiceTypes.find(zc=zeroconf))
    ServiceBrowser(zeroconf, services, handlers=[__on_service_state_change])
    time.sleep(scan_time_seconds)
    zeroconf.close()
    return ssc_device_setup
