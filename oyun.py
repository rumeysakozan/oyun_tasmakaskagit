taskagitmakas=["taş","kağıt","makas"]
import random
taş=taskagitmakas[0]
kağıt=taskagitmakas[1]
makas=taskagitmakas[2]
a=random.choice(taskagitmakas)
print("bilgisayar", a,"seçti")

while True:
    print("çıkmak için 'q' e basın.")
    gir=input("Taş mı? Kağıt mı? Makas mı? : ")
   
    if gir==kağıt:
        if kağıt==a:
            print("berabere")
        elif taş==a:
            print("kazandınız")
        elif makas==a:
            print("kaybettiniz")
            
    elif gir==taş:
        if taş==a:
            print("berabere")
        elif kağıt==a:
            print("kaybettiniz")
        elif makas==a:
            print("kazandınız")
            
    elif gir==makas:
        if makas==a:
            print("berabere")
        elif taş==a:
            print("kaybettiniz")
        elif kağıt==a:
            print("kazandınız")    
    else:
        print("oyun bitti.")
        break        
