from json import loads
from env import data

def openFileJson():
    # array sebagai penampung dari data json
    datasList = []

    # membuka file data.txt, dan merubahnya menjadi dictionary value
    with open(data['jsonPath2'], "r") as f:
            json_object = loads(f.read())
            for x in json_object:
                datasList.append(x)

    return datasList