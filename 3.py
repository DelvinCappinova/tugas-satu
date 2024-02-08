uang = 200000000
bunga = 10
x = uang
tahun = 0 
while x <= 400000000:
  tahun = tahun+1
  x = float(x*((100+bunga)/100))

y = float(round(x))
print (f"Waktu yang dibutuhkan adalah {tahun} tahun untuk merubah Rp.200000000 menjadi Rp.{y}")
