# 1) Bir aracın yakıt tipine göre (benzin,dizel,lpg) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu hesaplayan uygulamayı yapınız.
# benzin    : 39.35
# dizel     : 41.71
# lpg       : 20.28
#benzin=39.35
#dizel=41.71
#lpg=20.28
#mesafe=int(input("gidilen yol:"))
#benzinMasrafı=(mesafe*benzin)
#print(benzinMasrafı)
#dizelMasrafı=(mesafe*dizel)
#print(dizelMasrafı)
#lpgMasrafı=(mesafe*lpg)
#print(lpgMasrafı)


# 2) Bir öğrencinin 2 vize 1 final notunu alarak ortalama hesaplayınız ve hesaplanan ortalamaya göre not aralığına karşılık gelen harf notunu yazdırınız.
#    90-100 => AA
#    80-89  => BA
#    70-79  => BB
#    60-69  => CB
#    50-59  => CC
#    40-49  => DC
vize1Notu=int(input("1. vize notunuz:"))
vize2Notu=int(input("2. vize notunuz:"))
finalNotu=int(input("Final notunuz:"))
ortalama=(vize1Notu+vize2Notu+finalNotu)/3
if(90<=ortalama<=100):
     print("AA")
elif(80<=ortalama<=89):
    print("BA")
elif(70<=ortalama<=79):
    print("BB")
elif(60<=ortalama<=69):
    print("CB")
elif(50<=ortalama<=59):
    print("CC")
elif(40<=ortalama<=49):
    print("DC")