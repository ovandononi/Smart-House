import unittest
from src.sensor import Sensor
from src.devices import DeviceTV, DeviceLights, DeviceFireAlarm, DeviceCurtain, EmailSubscriber
from tests.test_data import *


class Test(unittest.TestCase):

    def test_turn_on_a_sensor_move(self):
        sensor_test = Sensor(1, "move", "Sensor on the front door", "Sensor", "off")
        device_light1 = DeviceLights(1, "light living room", "Device in the living room",
                                     "DeviceLights", "True", "off", "High")
        device_tv1 = DeviceTV(2, "TV living room", "Device in the living room",
                              "DeviceTV", "True", "off", 2)
        device_light2 = DeviceLights(3, "Lamp living room", "Device in the living room",
                                     "DeviceLights", "True", "off", "Low")
        sensor_test.register(device_light1)
        sensor_test.register(device_tv1)
        sensor_test.register(device_light2)
        sensor_test.set_state("on")
        self.assertEqual(sensor_test.__str__(), SENSOR_1)
        self.assertEqual(sensor_test.observers[0].__str__(), DEVICE_1)
        self.assertEqual(sensor_test.observers[1].__str__(), DEVICE_2)
        self.assertEqual(sensor_test.observers[2].__str__(), DEVICE_3)

    def test_turn_on_a_sensor_light(self):
        sensor_test = Sensor(2, "light", "Sensor in the living room", "Sensor", "off")
        device_curtain1 = DeviceCurtain(5, "curtain living room", "Device in the window of the living room",
                                        "DeviceCurtain", "True", "off", 2)
        device_curtain2 = DeviceCurtain(6, "curtain Bedroom 1", "Device in the window of the Bedroom 1",
                                        "DeviceCurtain", "True", "off", 3)
        device_curtain3 = DeviceCurtain(7, "curtain kitchen", "Device in the window of kitchen",
                                        "DeviceCurtain", "True", "off", 1)
        sensor_test.register(device_curtain1)
        sensor_test.register(device_curtain2)
        sensor_test.register(device_curtain3)
        sensor_test.set_state("on")
        self.assertEqual(sensor_test.__str__(), SENSOR_2)
        self.assertEqual(sensor_test.observers[0].__str__(), DEVICE_2_1)
        self.assertEqual(sensor_test.observers[1].__str__(), DEVICE_2_2)
        self.assertEqual(sensor_test.observers[2].__str__(), DEVICE_2_3)

    def test_turn_on_a_sensor_fume_amd_Email(self):
        sensor_test = Sensor(4, "fume", "Sensor on the kitchen", "Sensor", "off")
        device_fume1 = DeviceFireAlarm(8, "fire alarm", "Device of the house", "DeviceFireAlarm", "True", "off", 10)

        device_email2 = EmailSubscriber(9, "fire email", "Email sends to fire team",
                                        "EmailSubscriber", "True", "off", "fire@template.com")

        sensor_test.register(device_fume1)
        sensor_test.register(device_email2)
        sensor_test.set_state("on")
        self.assertEqual(sensor_test.__str__(), SENSOR_3)
        self.assertEqual(sensor_test.observers[0].__str__(), DEVICE_3_1)
        self.assertEqual(sensor_test.observers[1].__str__(), DEVICE_3_2)

    def test_turn_off_a_sensor_move(self):
        sensor_test = Sensor(1, "move", "Sensor on the front door", "Sensor", "on")
        device_light1 = DeviceLights(1, "light living room", "Device in the living room",
                                     "DeviceLights", "True", "on", "High")
        device_tv1 = DeviceTV(2, "TV living room", "Device in the living room",
                              "DeviceTV", "True", "on", 2)
        device_light2 = DeviceLights(3, "Lamp living room", "Device in the living room",
                                     "DeviceLights", "True", "on", "Low")
        sensor_test.register(device_light1)
        sensor_test.register(device_tv1)
        sensor_test.register(device_light2)
        sensor_test.set_state("off")
        self.assertEqual(sensor_test.__str__(), SENSOR_4)
        self.assertEqual(sensor_test.observers[0].__str__(), DEVICE_4_1)
        self.assertEqual(sensor_test.observers[1].__str__(), DEVICE_4_2)
        self.assertEqual(sensor_test.observers[2].__str__(), DEVICE_4_3)

    def test_turn_off_a_sensor_light(self):
        sensor_test = Sensor(2, "light", "Sensor in the living room", "Sensor", "on")
        device_curtain1 = DeviceCurtain(5, "curtain living room", "Device in the window of the living room",
                                        "DeviceCurtain", "True", "on", 2)
        device_curtain2 = DeviceCurtain(6, "curtain Bedroom 1", "Device in the window of the Bedroom 1",
                                        "DeviceCurtain", "True", "on", 3)
        device_curtain3 = DeviceCurtain(7, "curtain kitchen", "Device in the window of kitchen",
                                        "DeviceCurtain", "True", "on", 1)
        sensor_test.register(device_curtain1)
        sensor_test.register(device_curtain2)
        sensor_test.register(device_curtain3)
        sensor_test.set_state("off")
        self.assertEqual(sensor_test.__str__(), SENSOR_5)
        self.assertEqual(sensor_test.observers[0].__str__(), DEVICE_5_1)
        self.assertEqual(sensor_test.observers[1].__str__(), DEVICE_5_2)
        self.assertEqual(sensor_test.observers[2].__str__(), DEVICE_5_3)

    def test_turn_off_a_sensor_fume_amd_Email(self):
        sensor_test = Sensor(4, "fume", "Sensor on the kitchen", "Sensor", "on")
        device_fume1 = DeviceFireAlarm(8, "fire alarm", "Device of the house", "DeviceFireAlarm", "True", "on", 10)

        device_email2 = EmailSubscriber(9, "fire email", "Email sends to fire team",
                                        "EmailSubscriber", "True", "on", "fire@template.com")

        sensor_test.register(device_fume1)
        sensor_test.register(device_email2)
        sensor_test.set_state("off")
        self.assertEqual(sensor_test.__str__(), SENSOR_6)
        self.assertEqual(sensor_test.observers[0].__str__(), DEVICE_6_1)
        self.assertEqual(sensor_test.observers[1].__str__(), DEVICE_6_2)

    def test_turn_on_a_sensor_move_however_all_devices_were_unsubscribed(self):
        sensor_test = Sensor(1, "move", "Sensor on the front door", "Sensor", "off")
        device_light1 = DeviceLights(1, "light living room", "Device in the living room",
                                     "DeviceLights", "False", "off", "High")
        device_tv1 = DeviceTV(2, "TV living room", "Device in the living room",
                              "DeviceTV", "False", "off", 2)
        device_light2 = DeviceLights(3, "Lamp living room", "Device in the living room",
                                     "DeviceLights", "False", "off", "Low")
        sensor_test.register(device_light1)
        sensor_test.register(device_tv1)
        sensor_test.register(device_light2)
        sensor_test.set_state("on")
        self.assertEqual(sensor_test.__str__(), SENSOR_7)
        self.assertEqual(sensor_test.observers[0].__str__(), DEVICE_7_1)
        self.assertEqual(sensor_test.observers[1].__str__(), DEVICE_7_2)
        self.assertEqual(sensor_test.observers[2].__str__(), DEVICE_7_3)

    def test_turn_on_a_sensor_move_however_a_device_is_unsubscribed(self):
        sensor_test = Sensor(1, "move", "Sensor on the front door", "Sensor", "off")
        device_light1 = DeviceLights(1, "light living room", "Device in the living room",
                                     "DeviceLights", "False", "off", "High")
        device_tv1 = DeviceTV(2, "TV living room", "Device in the living room",
                              "DeviceTV", "True", "off", 2)
        device_light2 = DeviceLights(3, "Lamp living room", "Device in the living room",
                                     "DeviceLights", "False", "off", "Low")
        sensor_test.register(device_light1)
        sensor_test.register(device_tv1)
        sensor_test.register(device_light2)
        sensor_test.set_state("on")
        self.assertEqual(sensor_test.__str__(), SENSOR_8)
        self.assertEqual(sensor_test.observers[0].__str__(), DEVICE_8_1)
        self.assertEqual(sensor_test.observers[1].__str__(), DEVICE_8_2)
        self.assertEqual(sensor_test.observers[2].__str__(), DEVICE_8_3)
