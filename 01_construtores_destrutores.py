class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe ...")
        self.nome = nome
        self.cor = cor
        self. acordado = acordado

    def __del__(self):
        print("Removendo a instância da classe.")

    def falar(self):
        print("auau")


c = Cachorro("Chappie", "Amarelo")
c.falar()