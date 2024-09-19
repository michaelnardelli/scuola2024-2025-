class persona():
    def __init__(self,nome, cognome):
        self.__nome = nome
        self.__cognome = cognome
    def __str__(self):
        print(f"nome:{self.__nome} congome:{self.__cognome}")
    def info(self):
        print("ciao mi chiamo {self.__nome}")

info()



