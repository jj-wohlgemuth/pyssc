import pyssc as ssc
import os


if os.path.exists('setup.json'):
    found_setup = ssc.Ssc_device_setup()
    found_setup.from_json('setup.json')
else:
    found_setup = ssc.scan()
    if found_setup is not None:
        found_setup.to_json('setup.json')
    else:
        raise Exception("No SSC device setup found.")
found_setup.connect_all()
for _ in range(100):
    found_setup.send_all('{"audio":{"out":{"mute":true}}}', interface='')
    found_setup.send_all('{"audio":{"out":{"mute":false}}}', interface='')
found_setup.disconnect_all()
