from saque import saque

valor = int(input("Informe o valor que deseja sacar: "))
notas = saque(valor)

if notas is not None:
    for chave, valor in notas.items():
        if valor != 0:
            print(f"{valor} nota(s) de {chave}")
else:
    print("Saque indisponível para esse valor.")