import time
from src.reader_file import ReaderFile
from src.sensor import Sensor
from src.devices import DeviceTV, DeviceLights, DeviceFireAlarm, DeviceCurtain, EmailSubscriber
from src.printer import Printer


class SmartHouse(object):

    def __init__(self):
        self.sensors = {}
        self.devices = {}
        self.reader = ReaderFile()
        self.config_data = None

    def start_notifying_event(self):
        continue_running = True
        self.set_data()
        while continue_running:
            self.update_data()
            time.sleep(10)  # N seconds
            Printer().print_message("----------------------New Updated---------------------------")

    def set_data(self):
        self.config_data = self.reader.get_config_data()

        for device in self.config_data.get("subscribers"):

            if device["type"] == "DeviceLights":
                aux_device = DeviceLights(device["id"], device["name"], device["description"],
                                          device["type"], device["subscriber"], device["status"], device["intensity"])
                self.devices[aux_device.device_id] = aux_device
            elif device["type"] == "DeviceTV":
                aux_device = DeviceTV(device["id"], device["name"], device["description"],
                                      device["type"], device["subscriber"], device["status"], device["proximity"])
                self.devices[aux_device.device_id] = aux_device
            elif device["type"] == "DeviceCurtain":
                aux_device = DeviceCurtain(device["id"], device["name"], device["description"], device["type"],
                                           device["subscriber"], device["status"], device["number_curtain"])
                self.devices[aux_device.device_id] = aux_device
            elif device["type"] == "DeviceFireAlarm":
                aux_device = DeviceFireAlarm(device["id"], device["name"], device["description"],
                                             device["type"], device["subscriber"], device["status"], device["minutes"])
                self.devices[aux_device.device_id] = aux_device
            elif device["type"] == "EmailSubscriber":
                aux_device = EmailSubscriber(device["id"], device["name"], device["description"],
                                             device["type"], device["subscriber"], device["status"], device["email"])
                self.devices[aux_device.device_id] = aux_device

        for sensor in self.config_data.get("sensors"):
            aux_sensor = Sensor(sensor["id"], sensor["name"], sensor["description"],
                                sensor["type"], sensor["status"])
            for device in sensor["devices"]:
                aux_sensor.register(self.devices[device])
            self.sensors[aux_sensor.sensor_id] = aux_sensor

    def update_data(self):
        self.config_data = self.reader.get_config_data()
        for sensor in self.config_data.get("sensors"):
            Printer().print_message('{:-<30}'.format('Sensor:'))
            Printer().print_message(self.sensors[sensor["id"]].__str__())
            self.sensors[sensor["id"]].set_state(sensor["status"])
