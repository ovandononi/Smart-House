from src.printer import Printer


class Sensor(object):

    def __init__(self, sensor_id, sensor_name, sensor_description, sensor_type, sensor_state):
        """
                Initialize a list of observers.
        """
        self.sensor_id = sensor_id
        self.sensor_name = sensor_name
        self.sensor_description = sensor_description
        self.sensor_type = sensor_type
        self.sensor_state = sensor_state
        self.observers = []

    def set_state(self, value):
        """
        Override to notify observers of state
        changes when the state is updated.
        """
        self.sensor_state = value
        self.notify_observers()

    def register(self, observer):
        """
        Add an observer to the list of observers
        to be notified of state changes.
        """
        if observer not in self.observers:
            self.observers.append(observer)

    def deregister(self, observer):
        """
        Remove an observer.
        """
        self.observers.remove(observer)

    def notify_observers(self):
        """
        Iterate through observers and call the
        update() method on each one.
        """
        for observer in self.observers:
            if observer.is_subscriber == "True":
                observer.update(self.sensor_state)
            Printer().print_message(observer.__str__())

    def __str__(self):
        return '{} {} {} {}'.format("ID Sensor: " + str(self.sensor_id),
                                    " Name: " + self.sensor_name,
                                    " Description: " + self.sensor_description,
                                    " State: " + self.sensor_state)
