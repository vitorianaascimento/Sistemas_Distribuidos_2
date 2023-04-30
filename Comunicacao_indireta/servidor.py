import Pyro4

@Pyro4.expose
class MathService(object):
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

daemon = Pyro4.Daemon()
uri = daemon.register(MathService)
print("URI do objeto:", uri)

daemon.requestLoop()
