class Device(object):

    def __init__(self, device_id, device_name, device_description, device_type, is_subscriber, device_state):
        self.device_id = device_id
        self.device_name = device_name
        self.device_description = device_description
        self.device_type = device_type
        self.is_subscriber = is_subscriber
        self.device_state = device_state

    def update(self, value):
        """
        Update observer state.
        """
        raise NotImplementedError("update() is not implemented.")

    def __str__(self):
        return '{} {} {} {} {}'.format("ID Device: " + str(self.device_id),
                                       " Name: " + self.device_name,
                                       " Description: " + self.device_description,
                                       " Type: " + self.device_type,
                                       " State: " + self.device_state)


class DeviceTV(Device):

    def __init__(self, device_id, device_name, device_description, device_type, is_subscriber, device_state, proximity):
        super().__init__(device_id, device_name, device_description, device_type, is_subscriber, device_state)
        self.proximity = proximity

    def update(self, value):
        self.device_state = value

    def __str__(self):
        return '{} {}'.format(super().__str__(), " Proximity: " + str(self.proximity) + " meters")


class DeviceLights(Device):

    def __init__(self, device_id, device_name, device_description, device_type, is_subscriber, device_state, intensity):
        super().__init__(device_id, device_name, device_description, device_type, is_subscriber, device_state)
        self.intensity = intensity

    def update(self, value):
        self.device_state = value

    def __str__(self):
        return '{} {}'.format(super().__str__(), " Intensity: " + self.intensity)


class DeviceFireAlarm(Device):

    def __init__(self, device_id, device_name, device_description, device_type, is_subscriber, device_state, minutes):
        super().__init__(device_id, device_name, device_description, device_type, is_subscriber, device_state)
        self.minutes = minutes

    def update(self, value):
        self.device_state = value

    def __str__(self):
        return '{} {}'.format(super().__str__(), " Minutes: " + str(self.minutes))


class DeviceCurtain(Device):

    def __init__(self, device_id, device_name, device_description, device_type, is_subscriber,
                 device_state, number_curtain):
        super().__init__(device_id, device_name, device_description, device_type, is_subscriber, device_state)
        self.number_curtain = number_curtain

    def update(self, value):
        self.device_state = value

    def __str__(self):
        return '{} {}'.format(super().__str__(), " Number Of Curtain: " + str(self.number_curtain))


class EmailSubscriber(Device):

    def __init__(self, device_id, device_name, device_description, device_type, is_subscriber, device_state, email):
        super().__init__(device_id, device_name, device_description, device_type, is_subscriber, device_state)
        self.email = email

    def update(self, value):
        self.device_state = value

    def __str__(self):
        return '{} {}'.format(super().__str__(), " Email: " + self.email)
