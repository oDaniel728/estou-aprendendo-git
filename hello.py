from typing import List
import sys

class Main:
    def main(self, args: List[str]) -> None:
        self.print()
        
    def print(self) -> None:
        sys.stdout.write("Hello, World!\n")

def main(sys):
    if __name__ == "__main__":
        try:
            Main().main(sys.argv)
            return 0
        except Exception as e:
            sys.stderr.write("Error (" + str(e.__cause__.__class__.__name__) + ") => " + str(e))
            return 1
  
sys.stdout.write(str(main(sys)) + "\n")