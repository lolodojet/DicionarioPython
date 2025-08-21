nomes = ["Ana", "Carlos", "Maria"]

for tentativa in range(3):
    try:
        i = int(input("Digite o índice que quer imprimir: "))
        print(nomes[i])
    except ValueError:
        print("Valor inválido! Digite um número ")
    except IndexError:
        print("Valor inválido! Digite um número entre 0 e 2")
    finally:
        print(f"Tentativa {tentativa + 1}")