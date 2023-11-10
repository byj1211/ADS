class DeviceNotFoundError(Exception):
    def __init__(self, message='Device NotFound!'):
        self.message = message
