num = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
if num == num2:
    print(f"Os números são iguais!")
else:
    if num > num2:
        print(f"Em ordem crescente {num2}, {num}")
    else:
        print(f"Em ordem crescente {num}, {num2}")
