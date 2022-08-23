from env import data
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


#Program Isi Data
def program(data_set):
    #masuk website
    browser = webdriver.Chrome()
    actions = ActionChains(browser)
    browser.get(data['linkActive'])
    print('==== Welcome To Bangef, Automated Post-Test ====');

    try:
        for d in data_set:
            # mengecek apakah elemen input sudah ada dan mengisikannya
            # Nama
            WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, data['selectorById'][0]))
            ).send_keys(d['namaLengkap'])

            # Email
            WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, data['selectorById'][1]))
            ).send_keys(d['email'])

            # Nomer Telepon
            WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, data['selectorById'][2]))
            ).send_keys('0'+d['noTelpon'])

            # Jenis Kelamin
            elementJK = browser.find_element(By.ID, data['selectorById'][3])
            Select(elementJK).select_by_value(d['jk'])

            # Usia
            WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, data['selectorById'][4]))
            ).send_keys(d['usia'])

            # Pekerjaan
            elementPekerjaan = browser.find_element(By.ID, data['selectorById'][5])
            Select(elementPekerjaan).select_by_value(d['pekerjaan'])

            # Komunitas
            WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, data['selectorById'][6]))
            ).send_keys(d['organisasi'])

            # Pendidikan
            elementPendidikan = browser.find_element(By.ID, data['selectorById'][7])
            Select(elementPendidikan).select_by_value(d['pendidikan'])

            # Provinsi
            WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, data['selectorById'][8]))
            ).send_keys(d['provinsi'], Keys.RETURN)

            # Kota Asal
            elementCities = browser.find_element(By.ID, data['selectorById'][9])
            elementCities.send_keys(d['kotaAsal'], Keys.RETURN)

            # Captcha
            browser.execute_script("arguments[0].scrollIntoView();", elementCities)
            captcha = input('Masukan validasi captcha (sample : 9*9): \n');
            arr = list(captcha)
            if arr[1] == '+' :
                result = int(arr[0]) + int(arr[2])
            else :
                result = int(arr[0]) * int(arr[2])
            
            browser.find_element(By.ID, data['selectorById'][10]).send_keys(result)

            # Select Radio Button
            q1 = browser.find_element(By.ID, "1070-"+d['qSatu'])
            browser.execute_script("arguments[0].scrollIntoView();", q1)
            sleep(.5)
            q1.click()

            q2 = browser.find_element(By.ID, "1071-"+d['qDua'])
            browser.execute_script("arguments[0].scrollIntoView();", q2)
            q2.click()

            q3 = browser.find_element(By.ID, "1072-"+d['qTiga'])
            browser.execute_script("arguments[0].scrollIntoView();", q3)
            q3.click()

            q4 = browser.find_element(By.ID, "1073-"+d['qEmpat'])
            actions.move_to_element(q4).click().perform()
            browser.execute_script("arguments[0].scrollIntoView();", q4)
            sleep(.5)
            q4.click()

            q5 = browser.find_element(By.ID, "1076-"+d['qLima'])
            browser.execute_script("arguments[0].scrollIntoView();", q5)
            q5.click()

            # submit
            footer = browser.find_element(By.CSS_SELECTOR, '#__next > div > div.footer.mt-3')
            browser.execute_script("arguments[0].scrollIntoView();", footer)
            sleep(1)
            browser.find_element(By.XPATH, data['selectorByXpath']).click()
            sleep(3)    

            # kembali ke page sebelumnya
            browser.get(data['linkActive'])
            WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, data['selectorById'][0]))
            )
            print('Data dengan atas nama '+d['namaLengkap']+' berhasil ✔️')

        print('Total Data : '+ str(d['id']) +' Selesai Post Test')  

    except Exception as err:
        print('Data Selesai Terakhir : "id": "'+str(d['id'])+'".')  
        print(err)
        browser.quit()


