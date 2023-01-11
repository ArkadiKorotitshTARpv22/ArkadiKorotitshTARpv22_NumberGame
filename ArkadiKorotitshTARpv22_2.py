
print("*** Arvuge mäng ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = abs(int(input("Sisesta täisarv => ")))
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
    c=b=a
    paaris=0
    paaritu=0
    while b > 0:
            if b % 2 == 0:
                paaris+=1
            else:
                paaritu+=1
            b = b//10
    print("paarilised numbrid:" , paaris)
    print("paaritu arv:" , paaritu)
    print()
    print("*flip* sisestatud number")
    print()
    b=0
    while a > 0:
        number = a % 10
        a = a // 10
        b = b * 10
        b += number
    print("*ümberpööratud* number", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Syracuse hüpoteesi kontrollimine")
    print()
    if c % 2 == 0:
        print("c on paariline arv. Jaga 2ga.")
    else:
        print("c on paaritu arv. Korruta 3, lisa 1 ja jaga 2ga.")
    while c != 1:
            if c % 2 == 0:
                    c = c / 2
            else:
                    c = (3*c + 1) / 2
            print(c, end=" ")
    print()
    print("Hüpotees on tõene")