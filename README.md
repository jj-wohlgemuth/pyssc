# pyssc
A Sennheiser Sound Control Protocol (SSC) Client Implementation for Python

## Introduction 

The [Sennheiser Sound Control Protocol](https://assets.sennheiser.com/global-downloads/file/9541/TI_1093_v2.0_Sennheiser_Sound_Control_Protocol_ew_D1_EN.pdf) is a specific adaption of Open Sound Control. Pyssc is a simple client implementation that allows users to discover SSC Devices in their networks and subsequently communicate with those Devices via SSC.

## Installation

Pyssc is published to [pypi.org/pyssc](https://pypi.org/project/pyssc/).


```
pip install pyssc
```

## Usage

Initially you will have to find out the IP Addresses of your SSC Devices. If you don't know them you can try and find them using [zeroconf](https://pypi.org/project/zeroconf/).

```py
import pyssc as ssc
found_setup = ssc.scan()
```

When you know all the IPs you can store the setup as a JSON file.

```py
found_setup.to_json('setup.json')
```

Here's an example setup JSON:

```json
{
    "Device 1": "fe80::2a36:38ff:fe60:7515",
    "Device 2": "fe80::2a36:38ff:fe60:784f",
}
```

Once you have defined your setups as a JSON you don't need to scan anymore. Simply import your setup at the beginning of your session.

```py
found_setup = ssc.Ssc_device_setup()
found_setup.from_json('setup.json')
```

Now you can send and receive SSC either to and from a single device
```py
device_1 = found_setup.ssc_devices[0]
ssc_transaction = device_1.send_ssc('{"audio":{"out":{"mute":true}}}')
```

or the whole setup.

```py
found_setup.send_all('{"audio":{"out":{"mute":true}}}')
```

Please note that Unix systems require you to specify the network interface. The default value here is "%eth0". On Windows you can specify an empty String as the Value for "interface".

```py
ssc_transaction = device_1.send_ssc('{"audio":{"out":{"mute":true}}}', interface = "")
```

To find out which commands work for your specific SSC Device please refer to the [SSC Documentation](https://assets.sennheiser.com/global-downloads/file/9541/TI_1093_v2.0_Sennheiser_Sound_Control_Protocol_ew_D1_EN.pdf).
