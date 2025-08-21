nomes = ["Ana", "Carlos", "Maria"]

for tentativa in range(3):
    try:
        i = int(input("Digite o índice que quer imprimir "))
        print(nomes[i])
    except ValueError:
        print("Digite um numero")
    except IndexError:
        print("Valor invalido, digite entre 0 e 2")