from functools import cache
from csapat import csapat
csapatok:list[csapat]=[]

def beolvas(filename:str, lista:list, osztaly, fejlec:bool=True):
    f=open(filename, encoding="UTF8")
    if fejlec: f.readline()
    for i in f:
        lista.append(osztaly(i))

def filebaIras(filename:str, data:list, header:str|None):
    f=open(filename, "w", encoding="UTF8")
    if header!=None:
        f.write(header)
    for i in data:
        f.write(i)
    f.close()

def adottEvVBorszagai(ev:int)->str:
    orszagok=[]
    for i in csapatok:
        if i.elso_reszvetel<=ev and i.utolso_reszvetel>=ev:
            orszagok.append(i.orszag)
    back_text=""
    while orszagok:
        back_text+="\n\t"
        for i in range(4):
            if not orszagok: return back_text
            back_text+=str(orszagok.pop(0)).ljust(14)
    return back_text

def tobbOrszagOsszesReszvetel(orszagok:list):
    db=0
    for i in csapatok:
        if i.orszag in orszagok:
            db+=i.reszvetelek_szama
    return db

@cache
def elsoVB():
    elso=csapatok[0].elso_reszvetel
    for i in csapatok[1:]:
        reszvet=i.elso_reszvetel
        if reszvet<elso:
            elso=reszvet
    return elso

def vilagbajnokOrszagokSzama():
    db=0
    for i in csapatok:
        if i.legjobb_eredmeny.count("Világbajnok")==1:
            db+=1
    return f"Eddig {db} ország csapata volt világbajnok"

def orszagLegjobbEredmenye(orszag:str)->str:
    for i in csapatok:
        if i.orszag==orszag:
            return orszag+" legjobb eredménye: "+i.legjobb_eredmeny

def orszagOttVoltAzElson(orszag:str):
    for i in csapatok:
        if i.orszag==orszag and i.elso_reszvetel<=elsoVB() and i.utolso_reszvetel>=elsoVB():
            return orszag+" ott volt az első VB-n."
    return orszag+" nem volt ott az első VB-n."

def legalabbXAlkalommal_Fileba(x)->str