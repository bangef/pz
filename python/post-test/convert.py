import csv, json

csvFilePath = r'model/csvFileTest.csv'
jsonFilePath = r'model/jsonFileTest.json'

def convert():
    data = []
    with open(csvFilePath, encoding='utf-8') as csvFile :
        csvReader = csv.DictReader(csvFile)
        for rows in csvReader:
            data.append(rows)

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf :
        jsonString = json.dumps(data, indent=4)
        jsonf.write(jsonString)

convert()