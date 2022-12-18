"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: David Fryc
email: df@emd.dk
discord: David F.#2019
"""

texty = [""" Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. """,
"""At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.""",
"""The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present."""]

users = {
"bob":"123",
"ann":"pass123",
"mike":"password123",
"liz":"pass123"
}
cara = 60*"-"

#print (users)

username = input("Zadej uzivatelske jmeno: ".upper()).casefold()
password = input("Zadej heslo: ".upper())

if users.get(username) == password:
    print(cara)
    print("Vitej v aplikaci,", username.title())
    print("K analyze jsou k dispozici tri texty:")
    print("1 - Text 1")
    print("2 - Text 2")
    print("3 - Text 3")
    print(cara)
    
    vybrany_text = int(input("Vybrany text: ".upper()))
    text = (texty[(int(vybrany_text))-1])

    #print (text)
    
    # #for text in range 
    if int(text) >= 0 and int(text) < 4:
    #if text in texts[text]:
        print(text)
        print(f"Budeme analyzovat text cislo {int(text)}")
        print(cara)
    else:
        print("tohle nepujde")






else:
    print("Bohuzel, zadane uzivatelske jmeno nebo heslo nejsou v databazi, ukoncuji...")