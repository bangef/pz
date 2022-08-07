const {
    pathcsv,
    pathjson
} = require('./env/env');

let csvToJson = require('convert-csv-to-json');

let fileInputName = pathcsv;
let fileOutputName = pathjson;

csvToJson.generateJsonFileFromCsv(fileInputName, fileOutputName);