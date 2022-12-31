import pyssc as ssc
import os
import time

if os.path.exists('setup.json'):
    found_setup = ssc.Ssc_device_setup()
    found_setup.from_json('setup.json')
else:
    found_setup = ssc.scan()
    if found_setup is not None:
        found_setup.to_json('setup.json')
    else:
        raise Exception("No SSC device setup found.")

found_setup.connect_all(interface='', timeout=1)

for ssc_device in found_setup.ssc_devices:
    # check availablity of connected attribute for backward compatibility
    if hasattr(ssc_device, 'connected'):
      if not ssc_device.connected:
        print ("device",ssc_device.ip,"is not reachable. Error messages is", ssc_device.error)

for x in range(0, -30 , -1):
  print("dimm:",x)
  found_setup.send_all('{"audio":{"out":{"dimm":'+f'{x:.1f}'+'}}}')

found_setup.send_all('{"audio":{"out":{"dimm":0.0}}}')
found_setup.disconnect_all()
