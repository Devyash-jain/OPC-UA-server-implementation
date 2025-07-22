from opcua import Server
from datetime import datetime
import time

server = Server()
server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")
server.set_server_name("Demo OPC UA Server")

uri = "http://example.com"
idx = server.register_namespace(uri)

objects = server.get_objects_node()
device = objects.add_object(idx, "MyDevice")
temp = device.add_variable(idx, "Temperature", 20.0)
temp.set_writable()

server.start()
print("OPC UA Server started at opc.tcp://0.0.0.0:4840/freeopcua/server/")

try:
    while True:
        current = temp.get_value()
        temp.set_value(current + 0.1)
        print(f"Temperature: {current + 0.1}")
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping server...")

finally:
    server.stop()
