class Interface:
    def __init__(self,nome,ip):
        self.nome=nome
        self.ip=ip
    
    def update(self,nome,ip):
        self.nome = nome
        self.ip = ip

    def imprime(self):
        print(self.nome + ":" + self.ip)