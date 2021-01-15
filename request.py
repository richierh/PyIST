import requests

response = requests.get("https://api.github.com/users/richie/repos")
# print (response.json())
import serial
from serial.tools import list_ports

ser = list_ports.comports()
print (ser)