# Emulate interfaces in python
"""An interface defines the required methods a subclass has to have"""


def get_methods(Class):
    """Return all the non-special callable methods of a class"""
    return {
        func
        for func in dir(Class)
        if callable(getattr(Class, func)) and not func.startswith("__")
    }


class InterfaceError(Exception):
    """Raised when an interface error occurs"""

    def __init__(self, message):
        """You can do something before super class is called"""
        super().__init__(message)


class Interface:
    """An Interface class to be inherited from"""
    def __init__(self, _class):
        difference = self.methods.difference(get_methods(_class))
        if difference:
            raise InterfaceError(
                f"Method(s) {difference} not found in interface: {self.__class__.__name__}"
            )


class EntityInterface(Interface):
    """Create an interface with a set called: methods"""
    methods = {"handle_mouse_up", "handle_mouse_down"}

class Ball():

    def __init__(self):
        pass

    def handle_mouse_down(self):
        print("mouse down has been pressed")

# Link Ball class to interface
EntityInterface(Ball)

ball = Ball()
ball.handle_mouse_down()
