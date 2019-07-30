# dhcpsnoop
DHCP snooper for augmentation of presence information in smart home applications.


### Installing

```
pip install dhcpsnoop
```

### Configure your trusted devices

Populate the trusted_devices list in snoop.conf with the devices you wish to trigger on.

```
trusted_devices:
    - 00:00:00:11:22:33
presence_debounce_time: 15.0
presence_times:
    - [06:00, 21:00]
```

### Run the task

Start the snooper in your terminal and test the trigger!

```
snoop.py -c dhcpsnoop/snoop.conf
```
