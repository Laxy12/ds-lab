import Pyro4


@Pyro4.expose
class Calculator(object):
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y


daemon = Pyro4.Daemon()
uri = daemon.register(Calculator)

print("Server URI:", uri)
print("Calculator server started. Press Ctrl+C to exit.")

try:
    daemon.requestLoop()
except KeyboardInterrupt:
    print("\nExiting Calculator server.")
finally:
    daemon.shutdown()

 
