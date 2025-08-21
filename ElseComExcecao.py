while True:
    try:
        v = int(input("Digite um número inteiro (0 sai): "))
        if v == 0:
            break
    except Exception:
        print("Valor inválido! Digite novamente")
    else:
        print("Parabéns, nenhuma exceção")
    finally:
        print("Executado sempre com break")