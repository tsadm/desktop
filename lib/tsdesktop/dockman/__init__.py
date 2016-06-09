from docker import Client

def getClient():
    return Client(version='auto', timeout=15)
