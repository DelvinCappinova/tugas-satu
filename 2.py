A1 = 25
B1 = 650000
C1 = 685000

Uang1 = int(A1*C1 - A1*B1)
Persen1 = float((Uang1*100)/(A1*B1))
print (f"Emas Gerald = {A1} gram \nKeuntungan pertama Gerald = Rp.{Uang1} \nPersen keuntungan pertama Gerald = {Persen1}%")
print ()

Beli = 15
A2 = A1 + Beli
B2 = 685000
C2 = 715000

Uang2 = int((A2*C2)-(A1*B1)-(Beli*B2))
Persen2 = float((Uang2*100)/((A1*B1)+(Beli*B2)))
print (f"Emas Gerald = {A2} gram \nKeuntungan kedua Gerald = Rp.{Uang2} \nPersen keuntungan kedua Gerald = {Persen2}%")
