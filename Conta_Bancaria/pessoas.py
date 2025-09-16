class Pessoas:
    def __init__(self, nome, cpf, email, telefone):
        self.name = nome
        self.cpf = cpf
        self.email = email
        self.phone = telefone
        
    def exibir_pessoas(self):
        print(f'Nome: {self.name} \nCPF: {self.cpf} \nEMAIL: {self.email} \nTELEFONE: {self.phone}')
        
