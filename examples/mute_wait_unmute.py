import pyssc as ssc
from pyssc import Ssc_device_setup
import os
import time

if os.path.exists('setup.json'):
    found_setup = Ssc_device_setup()
    found_setup.from_json('setup.json')
else:
    found_setup = ssc.scan()
    found_setup.to_json('setup.json')
found_setup.connect_all()
found_setup.send_all('{"audio":{"out":{"mute":true}}}', interface='')
time.sleep(2)
found_setup.send_all('{"audio":{"out":{"mute":false}}}', interface='')
found_setup.disconnect_all()
