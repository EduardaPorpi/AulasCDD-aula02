tipo = input("Com qual combustível o automovel foi abastecido? ")
litros = float(input("Quantos litros? "))

if tipo == "G":
    valor = 5.80 * litros
    print(f"O valor total gasto com GASOLINA foi R${valor}")

else:
    valorE = 4.90 * litros
    print(f"O valor total gasto com ETANOL foi R${valorE}")
