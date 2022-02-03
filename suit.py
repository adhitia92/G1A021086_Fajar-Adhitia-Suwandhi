import random

pilihan = ["gunting", "batu", "kertas"]



toggle = True
while toggle:
    komputer = random.choice(pilihan)
    print ("PERMAINAN SEDERHANA BATU,GUNTING,KERTAS")
    pemain = input("gunting, batu, kertas ? \npilihan player : ")
    if pemain == komputer:
        print("pilihan kom :", komputer)
        print("seri !!")
       
    elif pemain == "gunting":
        if komputer == "kertas":
            print("pilihan com:", komputer)
            print("kamu menang !!")
            
        elif komputer == "batu":
            print("pilihan com:",komputer)
            print("kamu kalah !!")
           
    elif pemain == "batu":
        if komputer == "gunting":
            print("pilihan com:",komputer)
            print("kamu menang !!")
            
        elif komputer == "kertas":
            print("pilihan com:",komputer)
            print("kamu kalah !!")
            
    elif pemain == "kertas":
        if komputer == "batu":
            print("pilihan com:",komputer)
            print("kamu menang !!")
           
        elif komputer == "gunting":
            print("pilihan com:",komputer)
            print("kamu kalah !!")
            
    lanjut = input("lanjut atau tidak (y/n) : ")
    if lanjut == "y":
        continue
    elif lanjut == "n":
        toggle = False