# Képiró Balázs dolgozat
import math
import random
nl:str = "\n\n"
def elso_feladat(): #Kérj be 1 páros számot a felhasználótól
    print(nl,"Első feladat\nKérj be 1 páros számot a felhasználótól",nl)
    n:int = int(input("Kérem írjon be egy páros számot:"))
    while n%2 != 0:
        n:int = int((input("Ez nem egy páros szám\nAdjon meg egy páros számot! ")))

def masodik_feladat():
    print(nl,"Második feladat\nÍrass ki a konzolra 13 db  [10, 150] zárt intervallumba eső véletlen számot. Hány 3-mal osztható van közöttük? A kiírás formátuma: „A számok között X db 3-mal osztható van!",nl)
    n = 0
    while n <= 13:
        szam = math.floor(random.random()*150+10)
        if szam%3==0:
            print(f"A szám ({szam}) hárommal osztható")
        n+=1

def harmadik_feladat(text:str,n:int):
    print(nl,"Harmadik feladat\nÍrj eljárást, mely paraméterként kap egy text szöveget, és egy N számot.",nl)
    if len(text)<n:
        print(f"Nincs {n} karakter!")
    else:
        karakter:str = text[n]
        nagybetus:str = karakter.upper()
        
        print(f"A szöveg {n}. karaktere a {karakter}. Nagybetűvé alakítva: {karakter} -" + karakter.upper()*3)

def negyedik_feladat():
    print(nl,"Írj metódust, mely neveket kér a felhasználótól, amíg a @ jelet nem kapja.\nHány nevet adott meg a felhasználó?",nl)
    n = 0
    user = ""
    while user != "@":
        user = input("Adjon meg egy nevet! ")
        n+=1
    print (f"A felhaszmáló {n} nevet adott meg.")

def otodik_feladat():
    gep_tippje:int = math.floor(random.random()*3+1)
    print(gep_tippje)
    
    print(nl,"Szimuláljuk a kő-papír-olló játékot.",nl)
    felhasznalo_tippje = (input("Kérem adja meg a tippjét\nKő, Papír vagy Olló? ")).lower()

    if felhasznalo_tippje == "kő" or felhasznalo_tippje == "ko":
        felhasznalo_tippje:int = 1
    if felhasznalo_tippje == "papír" or felhasznalo_tippje == "papir":
        felhasznalo_tippje:int = 2
    if felhasznalo_tippje == "olló" or felhasznalo_tippje == "ollo":
        felhasznalo_tippje:int = 3

        
    if felhasznalo_tippje == gep_tippje:
        print("döntetlen")
    elif felhasznalo_tippje == 1 and gep_tippje == 2  or felhasznalo_tippje == 2 and gep_tippje == 3 or felhasznalo_tippje == 3 and gep_tippje == 1:
        print("Ön vesztett")
    else:
        print("Ön nyert")
