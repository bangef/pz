import csv, json
from module.env import data

def convert():
    data_set = []
    with open(data['csvPath'], encoding='utf-8') as csvFile :
        csvReader = csv.DictReader(csvFile)
        for rows in csvReader:
            data_set.append(rows)

    with open(data['jsonPath'], 'w', encoding='utf-8') as jsonf :
        jsonString = json.dumps(data_set, indent=4)
        jsonf.write(jsonString)