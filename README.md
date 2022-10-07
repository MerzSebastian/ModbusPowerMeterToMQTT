# ModbusPowerMeterToMQTT
Small script to read modbus data from a power meter (ORNO OR-WE-517) and publish it to a mqtt broker to use it in Home Assistant

## How to connect your hardware
Get the cheapest rs-485 usb adapter on ebay. should be only a couple bucks.
Connect the usb adapter with the power meter like this
```
A <=> A
B <=> B
```

## How to run this script?
Frist you should install all the required python packages to run this script with the following command
```
pip3 install -r requirements.txt
```
After that you have to change the connection settings by editing the following poroperties

```
mqtt_user = "username"          // mqtt broker username
mqtt_password = "password"      // mqtt broker password
mqtt_server_address = "0.0.0.0" // mqtt broker ip address
mqtt_server_port = 1883         // mqtt broker port
serial_port = "/dev/ttyUSB0"    // rs485 usb adapter port
interval = 2                    // how often should be published?
```

To test if it works you can simply run 

```
python3 ./ModbusPowerMeterToMQTT.py
```
and see if the broker recieves data.


If your test is successfull you should add the script to the cron job scheduler so that it is run on every restart. 
You can open the cron job scheduler by entering:

```
crontab -e
```

at the bottom you have to add the following
```
@reboot python3 /<YOUR_PATH>/ModbusPowerMeterToMQTT.py &
```

Save and close the file and confirm the entry by executing
```
crontab -l
```

Reboot and see if it works! :) 


## Home Assistant Integration

Add the following to your configuration.yaml (sensor section)

```
mqtt:
  sensor:
    - name: "power meter - voltage l1"
      state_topic: "power-meter/voltage/l1"
      unit_of_measurement: "V"
    - name: "power meter - voltage l2"
      state_topic: "power-meter/voltage/l2"
      unit_of_measurement: "V"
    - name: "power meter - voltage l3"
      state_topic: "power-meter/voltage/l3"
      unit_of_measurement: "V"
    - name: "power meter - frequency"
      state_topic: "power-meter/frequency"
      unit_of_measurement: "Hz"
    - name: "power meter - current"
      state_topic: "power-meter/current"
      unit_of_measurement: "A"
    - name: "power meter - current l1"
      state_topic: "power-meter/current/l1"
      unit_of_measurement: "A"
    - name: "power meter - current l2"
      state_topic: "power-meter/current/l2"
      unit_of_measurement: "A"
    - name: "power meter - current l3"
      state_topic: "power-meter/current/l3"
      unit_of_measurement: "A"
    - name: "power meter - wattage"
      state_topic: "power-meter/wattage"
      unit_of_measurement: "W"
    - name: "power meter - wattage l1"
      state_topic: "power-meter/wattage/l1"
      unit_of_measurement: "W"
    - name: "power meter - wattage l2"
      state_topic: "power-meter/wattage/l2"
      unit_of_measurement: "W"
    - name: "power meter - wattage l3"
      state_topic: "power-meter/wattage/l3"
      unit_of_measurement: "W"
    - name: "power meter - consumption"
      state_topic: "power-meter/consumption"
      unit_of_measurement: "kWh"
    - name: "power meter - wattage l1"
      state_topic: "power-meter/consumption/l1"
      unit_of_measurement: "kWh"
    - name: "power meter - wattage l2"
      state_topic: "power-meter/consumption/l2"
      unit_of_measurement: "kWh"
    - name: "power meter - wattage l3"
      state_topic: "power-meter/consumption/l3"
      unit_of_measurement: "kWh"
    - name: "power meter - power-factor l1"
      state_topic: "power-meter/power-factor/l1"
    - name: "power meter - power-factor l2"
      state_topic: "power-meter/power-factor/l2"
    - name: "power meter - power-factor l3"
      state_topic: "power-meter/power-factor/l3"
```

