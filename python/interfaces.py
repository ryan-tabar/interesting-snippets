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
    """Raised when an interface error occurs from a subclass"""

    def __init__(self, message):
        """You can do something before super class is called"""
        super().__init__(message)


class Interface:
    def __init__(self, _class):
        difference = self.methods.difference(get_methods(_class.__class__))
        if difference:
            raise InterfaceError(
                f"Method(s) {difference} not found in interface: {self.__class__.__name__}"
            )


class EntityInterface(Interface):
    methods = {"handle_mouse_up", "handle_mouse_down"}


class Ball:
    def __init__(self):
        """Link this class to an interface"""
        EntityInterface(self)

    def handle_mouse_down(self):
        print("mouse down has been pressed")


ball = Ball()
ball.handle_mouse_down()
