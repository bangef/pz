from module.program import program
from module.convert import convert
from module.openFileJson import openFileJson

def main():
    condition = True
    while condition :
        question = int(input('Pilih menu berikut :\n1. Convert File\n2. Automated Post-Test\nPilih Salah satu :\n'))
        if question == 1 :
            try:
                convert()
                print('==========================\nBerhasil Convert File')
            except Exception as err:
                print(err)
        elif question == 2 :
            try: 
                program(openFileJson())
            except Exception as err:
                print(err)
        else :
            condition = False
            print('Pilihan anda salah! Keluar Program')

main()