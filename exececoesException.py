nomes = ["Ana", "Carlos", "Maria"]

for tentativa in range(3):
    try:
        i = int(input("Digite o índice que quer imprimir "))
        print(nomes(i))
    except Exception as e:
        print(f"Algo de errado aconteceu {e}")