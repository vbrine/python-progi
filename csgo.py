class CsGo:
    def __init__(self,name,damage,price,acc,fr,type,poo):
      self.name=oszlop[0]
      self.damage=int(oszlop[1])
      self.price=int(oszlop[2])
      self.acc=float(oszlop[3])
      self.fr=float(oszlop[4])
      self.type=oszlop[5]
      self.poo=oszlop[6]
csgolista=[]
fajl=open("csgo.txt","r",encoding="utf-8")
fajl.readline()
for sor in fajl:
    oszlop=sor.strip().split(";")
    csgolista.append(CsGo(oszlop[0],oszlop[1],oszlop[2],oszlop[3],oszlop[4],oszlop[5],oszlop[6]))
for i in csgolista:
      print(f"{i.name} {i.damage} {i.price}$ {i.acc} {i.fr} {i.type} {i.poo}")
csgosorted=sorted(csgolista,key=lambda k:k.damage,reverse=True)
print("A tíz legjobb fegyver:")
for i in range(10):
    print(f"{csgosorted[i].name} {csgosorted[i].damage}dmg")