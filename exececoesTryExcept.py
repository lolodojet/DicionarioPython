try: 
    numero_float = float(input("Informe um numero"))
    print("Float numero ", numero_float)
    print(f"O resultado é {numero_float * 2: .2f}")
except:
    print("Não é um número")

