# importação de bibliotecas
from os import system, name as os_name
from time import sleep

# inicialização do produto
produto = {
    "Nome": "Feijão",
    "Quantidade": 100
}

# mudança de valores
produto["Quantidade"] = 200
produto["Nome"] = "Arroz"

# armazenamento de valores
nome = produto.get("Nome", "não encontrado")
quant = produto.get("Quantidade", -1)

# impressão dos valores

# impressão simples
print(f"Nome: {nome}, Quantidade: {quant}")

# / TODO: Enxugar mais o código