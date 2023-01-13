#!/usr/bin/python3
"""
square module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square implementation
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        init - constructor
        Args:
            size: size of the square
            x: x position
            y: y position
            id: id of the square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        overriden __str__ method
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, size):
        """ size setter """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        assigns attributes
        """
        lst = (self.id, self.size, self.x, self.y)
        if args:
            self.id, self.size, self.x, self.y = \
                    args + lst[len(args):len(lst)]
        else kwargs:
            for (key, value) in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        that returns the dictionary of a square.
        """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
