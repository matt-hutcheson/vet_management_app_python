class Client():
    def __init__(self, first_name, last_name, phone_number, address, registered=False, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.registered = registered
        self.id = id