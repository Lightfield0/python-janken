import random
import os

user_wins = 0
com_wins=0
ties=0

options = ['tas', 'kagit', 'makas']

while True:
    user_input = input("Tas, Kagit Yada Makas yaz veya çıkmak için Q tuşuna bas>> ").lower()
    if user_input == 'q':
        break

    # if user_input not in options:
    #     continue

    random_number = random.randint(0,2)

    com_pick=options[random_number]

    print("Rakip", com_pick , "secti")

    if user_input == com_pick:
        print('Berabere')
        ties = ties + 1

    elif user_input == 'tas' and com_pick =='makas':
        print("Kazandiniz!")
        user_wins+=1
        
    elif user_input == 'kagit' and com_pick =='tas':
        print("Kazandiniz!")
        user_wins+=1
       
    elif user_input == 'makas' and com_pick =='kagit':
        print("Kazandiniz!")
        user_wins+=1
    else:
        print("Kaybettiniz.")
        com_wins+=1
    
print("Su kadar",user_wins,"kazandiniz")
print("Su kadar",com_wins,"kaybettiniz")
print("Su kadar",ties,"berabere kaldınız")
print("Oyun bitti")
os.system("pause")
