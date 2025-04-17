import sys, re, typing

class Main:
    def main(self, args: typing.List[str]) -> None:
        self.input: str
        self.print()

    def print(self) -> None:
        # A string com valores hexadecimais
        input_str = "48 65 6c 6c 6f 2c 20 57 6f 72 6c 64 21\n"
        
        # Remove os espaços e converte os valores hexadecimais para caracteres ASCII
        hex_values = input_str.split()  # Dividir a string em uma lista com base nos espaços
        
        # Converter os valores hexadecimais para seus respectivos caracteres
        output = "".join(chr(int(hex_val, 16)) for hex_val in hex_values)
        
        # Exibir o resultado final
        sys.stdout.write(output + "\n")

def main(sys):
    if __name__ == "__main__":
        try:
            Main().main(sys.argv)
            return 0
        except Exception as e:
            sys.stderr.write("Error (" + str(e.__cause__.__class__.__name__) + ") => " + str(e))
            return 1
  
sys.stdout.write(str(main(sys)) + "\n")
