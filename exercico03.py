time = input("time 1: ")
gols1 = int(input(f"quantos gols {time} fez? "))

time2 = input("time 2:  ")
gols2 = int(input(f"quantos gols {time2} fez? "))

if gols1 == gols2:
    print(f"EMPATE ente {time} e {time2}")
else:
    if gols1 > gols2:
        print(f"O {time} foi VENCEDOR com {gols1}")
    else:
        print(f"O {time2} foi VENCEDOR com {gols2}")
