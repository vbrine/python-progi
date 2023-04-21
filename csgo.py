class CsGo:
    def __init__(self,name,damage,price,acc,fr,type,poo):
      self.name=oszlop[0]
      self.damage=int(oszlop[1])
      self.price=int(oszlop[2])
      self.acc=float(oszlop[3])
      self.fr=float(oszlop[4])
      self.type=oszlop[5]
      self.poo=oszlop[6]
csgo=[]
fajl=open("csgo.txt","r",encoding="utf-8")
readline()
for sor in fajl:
    oszlop=sor.strip().split(";")
    csgo.append(CsGo(oszlop[0],oszlop[1],oszlop[2],oszlop[3],oszlop[4],oszlop[5],oszlop[6]))
