"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """initializes both start and count attributres"""
        self.start = start
        self.count = start

    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.start + 1}>"

    def generate(self):
        """prints out the current serial number and incremennts it once after first call"""
        if self.count == self.start:
            msg = self.start
        else:
            msg = self.count
        self.count += 1
        return msg

    def reset(self):
        """resets count back to start"""
        self.count = self.start
