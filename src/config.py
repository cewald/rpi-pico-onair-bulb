import ujson

data = ''

def load_config():
    global data
    with open("src/config.json", "r") as file:
        data = ujson.load(file) 
    return data

def get_config():
    return data

