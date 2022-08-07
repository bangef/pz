const fs = require('fs');
const {
    pathjson
} = require('../env/env');
const dataPath = require('../' + pathjson);

//util functions
// menyimpan data
const saveData = (data) => {
    const stringyfyData = JSON.stringify(data);
    fs.writeFileSync('../' + pathjson, stringyfyData);
}

// mendapatkan semua data
const getAllData = () => {
    const jsonData = JSON.stringify(dataPath);
    return JSON.parse(jsonData)
}

// menghapus data
const deleteData = (dataId) => {
    fs.readFile('../' + pathjson, 'utf-8', (err) => {
        var existData = getAllData();
        const index = dataId + 1;
        delete existData[index];
        saveData(existData);
        console.log(`Data ${index} berhasil dihapus ❌`);
    });
}

const newLocal = 98;
deleteData(newLocal);
console.log(getAllData().length);

module.exports = {
    deleteData,
    getAllData
};