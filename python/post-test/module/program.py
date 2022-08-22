from module.env import data
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# import time, json


# pathJson = "model/jsonFileTest.json"
# array sebagai penampung dari data json
# datasList = []

# membuka file data.txt, dan merubahnya menjadi dictionary value
# with open(pathJson, "r") as f:
#         json_object = json.loads(f.read())
#         for x in json_object:
#             datasList.append(x)


data_set = {
        "id": "80",
        "namaLengkap": "Sumandi Sutrisno Fundrika",
        "email": "sumandiod@gmail.com",
        "noTelpon": "8576712837",
        "jk": "Laki-Laki",
        "usia": "27",
        "pekerjaan": "Freelancer",
        "organisasi": "Komunitas",
        "pendidikan": "10",
        "provinsi": "KALIMANTAN BARAT",
        "kotaAsal": "KOTA PONTIANAK",
        "qSatu": "d",
        "qDua": "d",
        "qTiga": "d",
        "qEmpat": "c",
        "qLima": "d"
    }

#Isi Data
def program():
    #masuk website
    browser = webdriver.Chrome()
    actions = ActionChains(browser)
    browser.get(data['linkActive'])
    print('==== Welcome To Bangef, Automated Post-Test ====');

    try:
        # for d in data:
            #iterator increment
            # data['iterator'] += 1

            # mengecek apakah elemen input sudah ada dan mengisikannya
            # Nama
            WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, data['selectorById'][0]))
            ).send_keys(data_set['namaLengkap'])

            # Email
            WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, data['selectorById'][1]))
            ).send_keys(data_set['email'])

            # Nomer Telepon
            WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, data['selectorById'][2]))
            ).send_keys('0'+data_set['noTelpon'])

            # Jenis Kelamin
            elementJK = WebDriverWait(browser, 10).until(
            EC.element_to_be_selected((By.ID, data['selectorById'][3]))
            )
            Select(elementJK).select_by_value(data_set['jk'])

            # Usia
            WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, data['selectorById'][4]))
            ).send_keys(data_set['usia'])

            # Pekerjaan
            elementPekerjaan = WebDriverWait(browser, 10).until(
            EC.element_to_be_selected((By.ID, data_set['selectorById'][5]))
            )
            Select(elementPekerjaan).select_by_value(data_set['pekerjaan'])

            # Komunitas
            WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, data['selectorById'][6]))
            ).send_keys(data_set['organisasi'])

            # Pendidikan
            elementPendidikan = WebDriverWait(browser, 10).until(
            EC.element_to_be_selected((By.ID, data_set['selectorById'][7]))
            )
            Select(elementPendidikan).select_by_value(data_set['pendidikan'])

            # Provinsi
            WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, data['selectorById'][8]))
            ).send_keys(data_set['provinsi'], Keys.RETURN)

            # Kota Asal
            elemenCities = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, data['selectorById'][9]))
            )
            elemenCities.send_keys(data_set['kotaAsal'], Keys.RETURN)
           
            # Captcha
            actions.move_to_element(elemenCities).perform()
            captcha = input('Masukan validasi captcha (sample : 9*9): \n');
            arr = list(captcha)
            if arr[1] == '+' :
                result = int(arr[0]) + int(arr[2])
            else :
                result = int(arr[0]) * int(arr[2])
            
            browser.find_element(By.ID, data['selectorById'][10]).send_keys(result)

            # Select Radio Button
            q1 = browser.find_element(By.ID, "1070-"+data_set['qSatu'])
            actions.move_to_element(q1).click().perform()
            # browser.execute_script("arguments[0].scrollIntoView();", q1)
            # time.sleep(.5)
            # q1.click()

            q2 = browser.find_element(By.ID, "1071-"+data_set['qDua'])
            actions.move_to_element(q2).click().perform()
            # browser.execute_script("arguments[0].scrollIntoView();", q2)
            # q2.click()

            q3 = browser.find_element(By.ID, "1072-"+data_set['qTiga'])
            actions.move_to_element(q3).click().perform()
            # browser.execute_script("arguments[0].scrollIntoView();", q3)
            # q3.click()

            q4 = browser.find_element(By.ID, "1073-"+data_set['qEmpat'])
            actions.move_to_element(q4).click().perform()
            # browser.execute_script("arguments[0].scrollIntoView();", q4)
            # time.sleep(.5)
            # q4.click()

            q5 = browser.find_element(By.ID, "1076-"+data_set['qLima'])
            actions.move_to_element(q5).click().perform()
            # browser.execute_script("arguments[0].scrollIntoView();", q5)
            # q5.click()

            

            # submit
            
            # footer = browser.find_element(By.CSS_SELECTOR, '#__next > div > div.footer.mt-3')
            # browser.execute_script("arguments[0].scrollIntoView();", footer)
            # time.sleep(1)
            # browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[2]/form/div[14]/button').click()
            # print('Data dengan "id": "'+ d['id'] +'" atas nama '+d['namaLengkap']+' berhasil ✔️')
            # time.sleep(3)    

            # # kembali ke page sebelumnya
            # browser.get('https://event.literasidigital.id/hadir/22749')
            # time.sleep(1)

        # print('Total Data : '+ str(i) +' Selesai Post Test')  

    except Exception as err:
        print(err)
        browser.quit()


