import gazu

gazu.set_host("http://192.168.1.14/api")
gazu.set_event_host("http://192.168.1.14")
gazu.log_in("admin@example.com", "admin@321")

print(gazu.client.host_is_valid())


def my_callback(data):
    print("Task status changed:")
    print(data)


def asset_created(data):
    print("new asset created")
    print(data)


try:
    event_client = gazu.events.init()
    gazu.events.add_listener(event_client, "task:status-changed", my_callback)
    gazu.events.add_listener(event_client, "asset:new", asset_created)
    gazu.events.run_client(event_client)
except KeyboardInterrupt:
    print("Stop listening.")
except TypeError:
    print("Authentication failed. Please verify your credentials.")
