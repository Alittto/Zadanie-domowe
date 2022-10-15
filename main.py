import main2


print("         KALKULATOR \n\n" +
      "1. v szeciana \n" +
      "2. v donut \n" +
      "3. v graniastoslupa trojkatnego \n" + 
      "4. v walca \n" +
      "5. v kuli \n" +
      "6. v stozka \n" + 
      "7. v piramidy \n \n")

while True:
    inp = int(input("wybierz co chcesz zrobic :  "))

    if inp == 1:
        print(ZadanieDomowe.v_szescian())
    elif inp == 2:
        a = float(input("podaj a: "))  
        print(ZadanieDomowe.v_donut())
    elif inp == 3:
        print(ZadanieDomowe.v_graniastoslup_trojkatny())
    elif inp == 4:
         r = float(input("podaj r: "))
         h = float(input("podaj h: "))
         print(ZadanieDomowe.v_walec(r, h))
    elif inp == 5:
        r = float(input("podaj r: "))
        print(ZadanieDomowe.v_kuli(r))
    elif inp == 6:
        r = float(input("podaj r: "))
        h = float(input("podaj h: "))
        print(ZadanieDomowe.v_stozek(r, h))
    elif inp == 7:
        a = float(input("podaj a: "))
        h = float(input("podaj h: "))
        print(ZadanieDomowe.v_piramidy(a, h))
    else:
        print("podales zla liczbe sprobuj ponownie! ")