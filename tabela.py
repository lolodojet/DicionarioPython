tabela = {"Alface": 0.45,
          "Batata": 1.20,
          "Tomate": 2.30,
          "Feijão": 1.50}

print("Preço alface:", tabela['Alface'])

print(tabela.keys())  
#printa todas as chaves

print(len(tabela))
#diz a quantidade de chaves

print(tabela.values())
#método que retorna os valores do dicionário, no caso os num q eu inseri

print(tabela.get('Tomate'))
#retorna o valor da chave no caso o 2.30
#É usado para recuperar o valor de uma chave, caso não exista ele diz "none"

