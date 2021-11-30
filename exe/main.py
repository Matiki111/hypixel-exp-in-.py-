poziom = int(input("Jaki poziom hypixela cię interesuje?: "))

mnoznik2 = poziom - 2
rel = 2500 * mnoznik2
lvl = float(10000 + rel)
boostery = float(lvl / 1000000)
cls = boostery * 50.57
bsg = boostery * 75.88
uhc = boostery * 60.69
war = boostery * 45.51
cvc = boostery * 40.44
tnt = boostery * 30.32

# boostery- ilosc boosterow na DANY poziom
# poziom - poziom ktory osoba wpisuje
# mnoznik2- poziom ktory osoba wpisuje odjety od 2(poziom 0 nie istnieje,a 1 nie ma wymaganej ilosci expa)
# lvl- ilosc expa na DANY poziom

if poziom == 1:
    print("Exp, który będziesz potrzebował, aby osiągnąć ten poziom to: 0")
elif poziom <= 0:
    print("wprowadź dane poprawnie!")
else:
    print("Exp, który będziesz potrzebował, aby osiągnąć ten poziom to: " + str(10000 + rel))
    lvl = float(10000 + rel)
    boostery = float(lvl / 1000000)


    print("Na ten konkretny level będziesz potrzebował ok.: " + (str(round(boostery,2))) + " boostera")



    wybor = int(input("Wybierz jaki booster chcialbys kupic wpisując:\n"
                  "1-classic games/arcade booster\n"
                  "2-blitz sg/mega walls/skywars booster\n"
                  "3-uhc champions booster\n"
                  "4-tnt games booster\n"
                  "5-warlords booster\n"
                  "6-smash heroes/cops and crims booster\n"))
    if wybor == 1:

        print("Będzie to " + str(round(cls, 2)) + "zł na ten konkretny lvl, jeżeli kupisz te boostery")
    elif wybor == 2:
        print("Będzie to " + str(round(bsg, 2)) + "zł na ten konkretny lvl, jeżeli kupisz te boostery")
    elif wybor == 3:
        print("Będzie to " + str(round(uhc, 2)) + "zł na ten konkretny lvl, jeżeli kupisz te boostery")
    elif wybor == 4:
        print("Będzie to " + str(round(tnt, 2)) + "zł na ten konkretny lvl, jeżeli kupisz te boostery")
    elif wybor == 5:
        print("Będzie to " + str(round(war, 2)) + "zł na ten konkretny lvl, jeżeli kupisz te boostery")
    elif wybor == 6:
        print("Będzie to " + str(round(cvc, 2)) + "zł na ten konkretny lvl, jeżeli kupisz te boostery")
    else:
        print("wpisz poprawny numer!")

input()




