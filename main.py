
poziom = int(input("Jaki poziom hypixela cię interesuje?: "))

mnoznik2 = poziom - 2
rel = 2500 * mnoznik2


if poziom == 1:
    print("Exp, który będziesz potrzebował, aby osiągnąć ten poziom to: 0")
else:
 print("Exp, który będziesz potrzebował, aby osiągnąć ten poziom to: " + str(10000 + rel))

 lvl = float(10000 + rel)
 boostery =  float(lvl / 1000000)

print("Na ten konkretny level będziesz potrzebował: " + (str(boostery)) + " boosterów")

input()

