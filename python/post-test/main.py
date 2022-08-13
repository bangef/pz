#import lib and ignore warning decepretion log
from warnings import filterwarnings
filterwarnings("ignore")
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time, json

pathJson = "model/jsonFileTest.json"
# array sebagai penampung dari data json
datasList = []

# membuka file data.txt, dan merubahnya menjadi dictionary value
with open(pathJson, "r") as f:
        json_object = json.loads(f.read())
        for x in json_object:
            datasList.append(x)

browser = webdriver.Chrome()

#Open Website
def directWeb():
    try:
        browser.set_window_size(500, 1000)
        browser.get('https://event.literasidigital.id/hadir/22467')
        time.sleep(1)


    except Exception as err:
        print(err)
        browser.quit()

#Isi Data
def fillInput(data):
    try:
        i = 0
        for d in data:
            
                
            i += 1
            # Nama Lengkap
            browser.find_element(By.ID, 'nama-lengkap').send_keys(d['namaLengkap'])

            # Email
            browser.find_element(By.ID, 'email').send_keys(d['email'])

            # Nomer Telepon
            browser.find_element(By.ID, 'no-hp').send_keys('0'+d['noTelpon'])

            # Jenis Kelamin
            Select(browser.find_element(By.ID, 'jenis-kelamin')).select_by_value(d['jk'])

            # Usia
            browser.find_element(By.ID, 'usia').send_keys(d['usia'])

            # Pekerjaan
            Select(browser.find_element(By.ID, 'pekerjaan')).select_by_value(d['pekerjaan'])

            # Komunitas
            browser.find_element(By.ID, 'komunitas').send_keys(d['organisasi'])

            # Pendidikan
            Select(browser.find_element(By.ID, 'pendidikan')).select_by_value(d['pendidikan'])

            # Provinsi
            browser.find_element(By.ID,'react-select-select-provice-input').send_keys(d['provinsi'], Keys.RETURN)

            # Kota Asal
            browser.find_element(By.ID,'react-select-select-cities-input').send_keys(d['kotaAsal'], Keys.RETURN)
           
            # Captcha
            browser.execute_script("arguments[0].scrollIntoView();", browser.find_element(By.ID,'react-select-select-cities-input'))
            captcha = input('Masukan validasi captcha (sample : 9*9): \n');
            arr = list(captcha)
            if arr[1] == '+' :
                result = int(arr[0]) + int(arr[2])
            else :
                result = int(arr[0]) * int(arr[2])
            
            browser.find_element(By.ID,'captcha').send_keys(result)
            # browser.find_element(By.ID, 'captcha').send_keys(result)

            # Select Radio Button
            q1 = browser.find_element(By.ID, "1070-"+d['qSatu'])
            browser.execute_script("arguments[0].scrollIntoView();", q1)
            time.sleep(.5)
            q1.click()

            q2 = browser.find_element(By.ID, "1071-"+d['qDua'])
            browser.execute_script("arguments[0].scrollIntoView();", q2)
            q2.click()

            q3 = browser.find_element(By.ID, "1072-"+d['qTiga'])
            browser.execute_script("arguments[0].scrollIntoView();", q3)
            q3.click()

            q4 = browser.find_element(By.ID, "1073-"+d['qEmpat'])
            browser.execute_script("arguments[0].scrollIntoView();", q4)
            time.sleep(.5)
            q4.click()

            q5 = browser.find_element(By.ID, "1076-"+d['qLima'])
            browser.execute_script("arguments[0].scrollIntoView();", q5)
            q5.click()

            

            # submit
            footer = browser.find_element(By.CSS_SELECTOR, '#__next > div > div.footer.mt-3')
            browser.execute_script("arguments[0].scrollIntoView();", footer)
            time.sleep(1)
            browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[2]/form/div[14]/button').click()
            print('Data dengan "id": "'+ d['id'] +'" atas nama '+d['namaLengkap']+' berhasil ✔️')
            time.sleep(2)    

            # kembali ke page sebelumnya
            browser.execute_script("window.history.go(-1)")
            time.sleep(2)

            #refresh apabila id kelipatan 0
            if int(d['id']) % 10 == 0 :
                browser.refresh()    

        print('Total Data : '+ str(i) +' Selesai Post Test')  


    except Exception as err:
        print(err)
        browser.quit()

# run program:
directWeb()
fillInput(datasList)

