nota = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
media = (nota + nota2 + nota3) / 3
if (nota < 0 or nota > 10) or (nota2 < 0 or nota2 > 10) or (nota3 < 0 or nota3 > 10):
    print(f"Informe os dados corretamentes")
else:
    if media >= 7.0:
        print(f"O aluno está APROVADO com média {media:.2f}")
    else:
        if media >= 4.0:
            print(f"O aluno está de RECUPERAÇÃO com média {media:.2f}")
        else:
            print(f"O aluno está REPROVADO com média {media:.2f}")
