import ujson

data = None


def get_config():
    global data
    if not data:
        print("Init config")
        with open("config.json", "r") as file:
            data = ujson.load(file)
    return data
