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
        self.start = start-1
        self.count= self.start

    def __repr__(self):
        return f'<SerialGenerator start={self.start+1} next ={self.count+1}'
    def generate(self):
        """incremenet the counter variable by one and return it"""
        self.count += 1
        return self.count
    def reset(self):
        """resets the counter variable to the start variable"""
        self.count=self.start

