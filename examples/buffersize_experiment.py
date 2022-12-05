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
dev = found_setup.ssc_devices[0]
command = '{"osc":{"schema":null}}'


for buf_size in [2**n for n in range(3, 9)]:
    ssc_transaction = dev.send_ssc(command,
                                   interface='',
                                   buffersize=buf_size,
                                   wait_time_seconds=.001*buf_size)
    print('buffersize: ' + str(buf_size))
    print('length of received string: ' + str(len(ssc_transaction.RX)))
    print('wait_time_seconds: ' + str(round(.001*buf_size, 3)))
