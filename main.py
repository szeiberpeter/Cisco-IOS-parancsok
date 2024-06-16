from focicsapatok import *
beolvas("fociVBk.csv", csapatok, csapat)

print(f"1. feladat: csapatok száma: {len(csapatok)}")
print(f"2. feladat: 2018-as VB csapatai:{adottEvVBorszagai(2018)}")
print(f"3. feladat: A BeNeLux oszágok összesen {tobbOrszagOsszesReszvetel(["Belgium", "Hollandia", "Luxemburg"])} alkalommal vettek részt a VB-n")
print(f"4. feladat: Az első VB-t {elsoVB()}-ban rendezték")
print(f"5. feladat: {vilagbajnokOrszagokSzama()}")
print(f"6. feladat: {orszagLegjobbEredmenye("Szlovákia")}")
print(f"6. feladat: {orszagOttVoltAzElson("Magyarország")}")