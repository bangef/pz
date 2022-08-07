// import env dari env
const {
    link,
    elId
} = require('./env/env');

const {
    deleteData,
    getAllData
} = require('./controller/ControllerApp')

const readline = require('readline')
    .createInterface({
        input: process.stdin,
        output: process.stdout
    });

const {
    Builder,
    Browser,
    By,
    Key,
} = require('selenium-webdriver');

let driver = new Builder().forBrowser(Browser.CHROME).build();

async function main() {
    try {
        await driver.get(link);

        getAllData().forEach((item) => {
            console.log(item.id);
        });
        /**
         * SAMPLE DUMY DATA
         */
        sendValue(elId.n, 'Nunik');
        sendValue(elId.e, 'Nunik@gmail.com');
        sendValue(elId.nh, '08998077520');
        sendValue(elId.jk, 'Laki-Laki');
        sendValue(elId.u, 35);
        sendValue(elId.p, 'Wirausaha');
        sendValue(elId.k, 'Komunitas');
        sendValue(elId.pe, 'D1');
        sendValue(elId.pr, 'ACEH');
        sendValue(elId.ka, 'KOTA SABANG');
        radioBtn(elId.q1);
        radioBtn(elId.q2);
        radioBtn(elId.q3);
        radioBtn(elId.q4);
        radioBtn(elId.q5);
        await driver.executeScript("arguments[0].scrollIntoView();", driver.findElement(By.id(elId.ka)));
        readline.question('Masukan validasi captcha (sample: 9*9):\n', (e) => {
            let result = e.split("");
            if (result[1] == '+') {
                result = parseInt(result[0]) + parseInt(result[2]);

            } else {
                result = parseInt(result[0]) * parseInt(result[2])
            }
            driver.executeScript(`document.getElementById("${elId.c}").value = ${result}`);
            readline.close();
        });

    } catch (err) {
        console.log(err);
        driver.quit();
    }
};

async function sendValue(id, value) {
    driver.findElement(By.id(id)).sendKeys(value, Key.RETURN);
};

async function radioBtn(id) {
    driver.executeScript(`document.getElementById("${id}").setAttribute("checked", "checked")`);
};

main();