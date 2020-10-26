import time
from src.reader_file import ReaderFile
from src.sensor_manager import SensorManager
from src.subscriber import DeviceSubscriber, EmailSubscriber
from src.printer import Printer


class SmartHouse(object):

    def __init__(self):
        self.sensors = []
        self.reader = ReaderFile()

    def start_notifying_event(self):
        continue_running = True
        self.set_data()
        while continue_running:
            self.update_data()
            for sensor in self.sensors:
                Printer().print_message(sensor.__str__())
                sensor.notify_observers()
            time.sleep(10)  # N seconds
            Printer().print_message("-------------------------------------------")

    def set_data(self):

        self.config_data = self.reader.get_config_data()
        for sensor in self.config_data.get("sensors"):
            aux_sensor = SensorManager(sensor["id"], sensor["name"], sensor["description"], sensor["type"], sensor["status"])
            for subscriber in self.config_data.get("subscribers"):
                if subscriber["subscriber"] == "True" and subscriber["sensorId"] == sensor["id"]:
                    if subscriber["type"] == "Device":
                        aux_device = DeviceSubscriber(subscriber["id"], subscriber["name"], subscriber["description"], subscriber["status"])
                        aux_sensor.register(aux_device)
                    elif subscriber["type"] == "Email":
                        aux_email_sub = EmailSubscriber(subscriber["id"], subscriber["name"], subscriber["description"], subscriber["status"], subscriber["email"])
                        aux_sensor.register(aux_email_sub)
            self.sensors.append(aux_sensor)

    def update_data(self):
        self.config_data = self.reader.get_config_data()
        for sensor in self.config_data.get("sensors"):
            for sensor_before in self.sensors:
                if sensor["id"] == sensor_before.sensor_id:
                    sensor_before.sensor_state = sensor["status"]
        #TODO update subscribers
