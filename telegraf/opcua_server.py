from opcua import Server, ua
import time
# Create a new OPC UA server
server = Server()

# Set the server endpoint URL and port
server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")
# Start the server
server.set_security_policy([
    ua.SecurityPolicyType.NoSecurity,
    ua.SecurityPolicyType.Basic256Sha256_SignAndEncrypt,
    ua.SecurityPolicyType.Basic256Sha256_Sign])

# server.start()

# Register a namespace
uri = "http://example.com"
idx = server.register_namespace(uri)
print(idx)
# Create a custom object
node = server.get_objects_node()

obj = node.add_object(idx, "MyObject1")

# Create a custom variable
var = obj.add_variable(idx, "MyVariable", 0.0)
var.set_writable()  # Enable write access for the variable

# Start the server
server.start()

print("OPC UA server is running!")

try:
    # Update the custom variable value periodically
    while True:
        value = var.get_value()
        print(value)
        value += 1.0
        var.set_value(value)
        time.sleep(5)
finally:
    server.stop()

