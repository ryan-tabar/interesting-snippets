# Emulate interfaces in python
"""An interface defines the required methods a subclass has to have"""
"""In this snippet, we are using inheritance to apply these requirements"""


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
        """Do something before super class is called"""
        super().__init__(message)


class Entity:

    methods = {"handle_mouse_up", "handle_mouse_down"}

    def __init__(self):
        difference = Entity.methods.difference(get_methods(self.__class__))
        print(Entity.methods)
        if difference:
            raise InterfaceError(
                f"Method(s) {difference} not found in class {self.__class__.__name__}"
            )


class Ball(Entity):
    def __init__(self):
        super().__init__()
        pass

    def handle_mouse_down(self):
        print("mouse down has been pressed")


ball = Ball()
ball.handle_mouse_down()
