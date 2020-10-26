from src.printer import Printer


class Subscriber(object):

    def __init__(self, subscriber_id, subscriber_name, subscriber_description, state):
        self.subscriber_id = subscriber_id
        self.subscriber_name = subscriber_name
        self.subscriber_description = subscriber_description
        self.state = state

    def update(self, value):
        """
        Update observer state.
        """
        raise NotImplementedError("update() is not implemented.")

    def __str__(self):
        return '{} {} {} {}'.format("ID Subscriber: " + str(self.subscriber_id),
                                    " Name: " + self.subscriber_name,
                                    " Description: " + self.subscriber_description,
                                    " State: " + self.state)


class DeviceSubscriber(Subscriber):

    def __init__(self, subscriber_id, subscriber_name, subscriber_description, state):
        super().__init__(subscriber_id, subscriber_name, subscriber_description, state)

    def update(self, value):
        self.state = value
        print(super().__str__())


class EmailSubscriber(Subscriber):

    def __init__(self, subscriber_id, subscriber_name, subscriber_description, state, email):
        super().__init__(subscriber_id, subscriber_name, subscriber_description, state)
        self.email = email

    def update(self, value):
        self.state = value
        Printer().print_message(super().__str__() + self.email)
