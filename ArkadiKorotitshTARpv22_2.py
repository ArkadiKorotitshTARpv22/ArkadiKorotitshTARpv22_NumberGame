
print("*** Arvuge mäng ***")#siin ma just tõlkisin
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = abs(int(input("Sisesta täisarv => ")))#siit eemaldasin lisasulud
        break
    except ValueError:
        print("See ei ole täisarv")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Nulliga pole mõtet midagi teha")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Määrake, mitu paarilist ja mitu paaritut numbrit on numbris")
    print()
    c=b=a#Siin eemaldasin lisamärgid =
    paaris=0#Siin eemaldasin lisamärgi =
    paaritu=0#Siin eemaldasin lisamärgi =
    while b > 0:
            if b % 2 == 0:#siia lisasin märgi =
                paaris+=1#siin vahetasin + ja = kohad
            else:
                paaritu+=1#siin vahetasin + ja = kohad
            b = b//10
    print("paarilised numbrid:" , paaris)#siia lisasin koma
    print("paaritu arv:" , paaritu)#siia lisasin koma
    print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*flip* sisestatud number")
    print()
    b=0
    while a > 0:
        number = a % 10
        a = a // 10
        b = b * 10
        b += number#siin vahetasin + ja = kohad
    print("*ümberpööratud* number", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Syracuse hüpoteesi kontrollimine")
    print()
    if c % 2 == 0:#siia lisasin märgi =
        print("c on paariline arv. Jaga 2ga.")
    else:
        print("c on paaritu arv. Korruta 3, lisa 1 ja jaga 2ga.")
    while c != 1:
            if c % 2 == 0:#siia lisasin märgi =
                    c = c / 2#Siin eemaldasin lisamärgi =
            else:
                    c = (3*c + 1) / 2#Siin eemaldasin lisamärgi =
            print(c, end=" ")
    print()
    print("Hüpotees on tõene")