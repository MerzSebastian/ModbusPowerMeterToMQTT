import minimalmodbus
import serial
import struct
import binascii
import paho.mqtt.client as mqtt
import time

mqtt_user = "username"
mqtt_password = "password"
mqtt_server_address = "0.0.0.0"
mqtt_server_port = 1883
serial_port = "/dev/ttyUSB0"
interval = 2

client = mqtt.Client()
client.username_pw_set(username="mqtt_user",password="mqtt_password")
client.connect(mqtt_server_address, mqtt_server_port, 60)
modbus = minimalmodbus.Instrument(serial_port, 1)
modbus.serial.baudrate = 9600
modbus.serial.bytesize = 8
modbus.serial.parity = serial.PARITY_EVEN
modbus.serial.stopbits = 1
modbus.serial.timeout = 0.6
modbus.mode = minimalmodbus.MODE_RTU
modbus.clear_buffers_before_each_transaction = False
modbus.debug = False

def convert(value, scale = 1):
    result=str(hex(value)).replace('0x', '')
    return round(struct.unpack('>f', binascii.unhexlify('00000000' if result == '0' else result))[0] * scale, 2)

while True:
    time.sleep(interval)
    client.publish("power-meter/voltage/l1", convert(modbus.read_long(14, 3, False, 0)))
    client.publish("power-meter/voltage/l2", convert(modbus.read_long(16, 3, False, 0)))
    client.publish("power-meter/voltage/l3", convert(modbus.read_long(18, 3, False, 0)))
    client.publish("power-meter/frequency", convert(modbus.read_long(20, 3, False, 0)))
    client.publish("power-meter/current", round(current_l1 + current_l2 + current_l3, 2))
    client.publish("power-meter/current/l1", convert(modbus.read_long(22, 3, False, 0)))
    client.publish("power-meter/current/l2", convert(modbus.read_long(24, 3, False, 0)))
    client.publish("power-meter/current/l3", convert(modbus.read_long(26, 3, False, 0)))
    client.publish("power-meter/wattage", convert(modbus.read_long(28, 3, False, 0), 1000))
    client.publish("power-meter/wattage/l1", convert(modbus.read_long(30, 3, False, 0), 1000))
    client.publish("power-meter/wattage/l2", convert(modbus.read_long(32, 3, False, 0), 1000))
    client.publish("power-meter/wattage/l3", convert(modbus.read_long(34, 3, False, 0), 1000))
    client.publish("power-meter/power-factor/l1", convert(modbus.read_long(54, 3, False, 0)))
    client.publish("power-meter/power-factor/l2", convert(modbus.read_long(56, 3, False, 0)))
    client.publish("power-meter/power-factor/l3", convert(modbus.read_long(58, 3, False, 0)))
    client.publish("power-meter/consumption", convert(modbus.read_long(256, 3, False, 0)))
    client.publish("power-meter/consumption/l1", convert(modbus.read_long(258, 3, False, 0)))
    client.publish("power-meter/consumption/l2", convert(modbus.read_long(260, 3, False, 0)))
    client.publish("power-meter/consumption/l3", convert(modbus.read_long(262, 3, False, 0)))