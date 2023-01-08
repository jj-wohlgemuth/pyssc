import pyssc as ssc
import os
import time

interface='en1'

if os.path.exists('setup.json'):
    found_setup = ssc.Ssc_device_setup()
    found_setup.from_json('setup.json')
else:
    found_setup = ssc.scan()
    if found_setup is not None:
        found_setup.to_json('setup.json')
    else:
        raise Exception("No SSC device setup found.")

found_setup.connect_all(interface='%'+interface, timeout=4)

for ssc_device in found_setup.ssc_devices:
    # check availablity of connected attribute for backward compatibility
    if hasattr(ssc_device, 'connected'):
      if not ssc_device.connected:
        print ("device",ssc_device.ip,"is not reachable. Error messages is", ssc_device.error)

print("Dimming speakers without reconnect")
for x in range(0, -30 , -1):
  print("dimm:",x)
  found_setup.send_all('{"audio":{"out":{"dimm":'+f'{x:.1f}'+'}}}')

print("Dimming speakers with reconnect")
for x in range(-29, 1 , 1):
  print("dimm:",x)
  
  # try to reconnect, if device is not connected
  for ssc_device in found_setup.ssc_devices:
    # check availablity of connected attribute for backward compatibility
    if hasattr(ssc_device, 'connected'):
      if not ssc_device.connected:
        print("reconnect device",ssc_device.ip)
        ssc_device.connect(interface='%'+interface, timeout=4)

  found_setup.send_all('{"audio":{"out":{"dimm":'+f'{x:.1f}'+'}}}')

found_setup.disconnect_all()
