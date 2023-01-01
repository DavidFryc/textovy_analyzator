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
soucet = 0

username = input("Enter your user name:\t".upper()).casefold()
password = input("Enter your password:\t".upper())

vysledek = {'pocet slov':0, 'prvni velke':0, 'vsechna velka':0, 'vsechna mala':0, "pocet cisel":0 }

# KONTROLA USER NAME A PASSWORD

if users.get(username) == password:
    print(cara)
    print("Welcome in app,", username.title())
    print("We have 3 texts to be analyzed:")
    print("1 - Text 1")
    print("2 - Text 2")
    print("3 - Text 3")
    print(cara)
    text = int(input("Selected text: ".upper()))-1
    
    #VYBER TEXTU

    if int(text) >= 0 and int(text) < 3:
        vybrany_text = texty[text]
        print (cara)
        pocet_vseho = len(texty[text].split())         
        
        split_text = texty[text].split()
                
        # for pocetslov in split_text:               #neni potreba, nezapocita slova koncici "." nebo ","
        #     if pocetslov.isalpha() is True:
        #         vysledek ['pocet slov'] +=1
        #     else:
        #         continue
        
        for prvnivelke in split_text:
            if prvnivelke.istitle() is True:
                vysledek ['prvni velke'] +=1
            else:
                continue

        for vsechnavelka in split_text:
            if vsechnavelka.isupper() is True:
                vysledek ['vsechna velka'] +=1
            else: 
                continue

        for vsechnamala in split_text:
            if vsechnamala.islower() is True:
                vysledek ['vsechna mala'] +=1
            else: 
                continue

        for cislo in split_text:
            if cislo.isdigit() is True:
                vysledek ['pocet cisel'] +=1
                soucet = soucet + int(cislo)
            else:
                continue
        
        pocet_vyskytu = []
        vyskytu_celkem = {}
        for pocet in split_text:
            pocet_vyskytu.append(len(pocet))
        for pocet_vysledek in pocet_vyskytu:
            if pocet_vysledek not in vyskytu_celkem:
                vyskytu_celkem[pocet_vysledek] = 1
            else:
                vyskytu_celkem[pocet_vysledek] = vyskytu_celkem[pocet_vysledek] + 1

        #print (vysledek)
        #print(pocet_vseho)
        print ("There are", pocet_vseho - vysledek['pocet cisel'],"words in the selected text.")
        #print ("There are", vysledek['pocet slov'],"words in the selected text.")
        print ("There are", vysledek['prvni velke'],"titlecase words.")
        print ("There are", vysledek['vsechna velka'],"uppercase words.")
        print ("There are", vysledek['vsechna mala'],"lowercase words.")
        print ("There are", vysledek['pocet cisel'],"numeric strings.")
        print ("The sum of all the numbers is", soucet)
        print(cara)
        print("LEN \t| COUNT\t| OCCURENCES.")

        for key, value in sorted(vyskytu_celkem.items()):
            print (key,"\t|", value,"\t|", "*"*value)
        print(cara)
    else:
        print (cara)
        print("Selected number is not in the database, terminating.".upper())
        print (cara)
    quit()

else:
    print (cara)
    print("Our deepest apology, unknown user name or password. Terminating...".upper())
    print (cara)
quit()