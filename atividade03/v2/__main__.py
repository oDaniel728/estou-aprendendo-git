from sys import *
from atividade03.v3.produto import Produto


class Main:
    def __init__(self, args: list[str]) -> None:
        self.main(args)

    def main(self, args: list[str]) -> None:
        # inicialização do produto
        produto = Produto("Feijão", 100)

        # mudança de valores
        produto.quantity = 200
        produto.name = "Arroz"

        # armazenamento de valores
        nome, quantidade, _ = list(produto)

        # impressão dos valores

        # impressão simples
        stdout.write("Nome: {}, Quantidade: {}\n".format(nome, quantidade))
        stdout.flush()
        
        stdin.read(1)
        
if __name__ == "__main__":
    Main(argv)